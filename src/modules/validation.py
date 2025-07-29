from abc import ABC, abstractmethod
import numpy as np
from typing import List, Dict, Set, Tuple
from src.bases import BaseValidation, BaseModelEncode, BaseSimilarity
from src.utils.reader import load_json
from src.utils.writer import save_json

class MatchingProcessor:
    """Handles matching between predicted and labeled data using similarity measures."""

    def __init__(self, model_encoder: BaseModelEncode, similar_method: BaseSimilarity, threshold: float = 0.5):
        """Initialize the MatchingProcessor.

        Args:
            model_encoder: Encoder to convert text to vectors.
            similar_method: Method to compute similarity between vectors.
            threshold: Similarity threshold for matching.
        """
        self.model_encoder = model_encoder
        self.similar_method = similar_method
        self.threshold = threshold

    def match_data(self, predict_data: List[Dict], label_data: List[Dict]) -> Tuple[int, int, Set[int]]:
        """Match predicted data with labeled data based on similarity.

        Args:
            predict_data: List of dictionaries containing predicted data.
            label_data: List of dictionaries containing ground truth labels.

        Returns:
            Tuple containing true positives, false positives, and set of matched label indices.
        """
        true_positives = 0
        false_positives = 0
        matched_labels = set()

        for pred in predict_data:
            best_match = None
            best_similarity = -1
            best_match_idx = -1
            pred_name_vec = self.model_encoder.text_encode(pred["Name"].lower().strip())

            for i, label in enumerate(label_data):
                if i in matched_labels:
                    continue
                label_name_vec = self.model_encoder.text_encode(label["Name"].lower().strip())
                similarity = self.similar_method.compute_similarity(pred_name_vec, label_name_vec)
                if similarity >= self.threshold and similarity > best_similarity:
                    best_similarity = similarity
                    best_match = label
                    best_match_idx = i

            if best_match and self._is_correct_match(pred, best_match):
                true_positives += 1
                matched_labels.add(best_match_idx)
            else:
                false_positives += 1

        return true_positives, false_positives, matched_labels

    def _is_correct_match(self, pred: Dict, label: Dict) -> bool:
        """Check if all fields between prediction and label match based on similarity.

        Args:
            pred: Dictionary containing predicted data.
            label: Dictionary containing ground truth label.

        Returns:
            True if all fields match above the threshold, False otherwise.
        """
        fields = ["Name", "Species", "Organisms", "Amount_of_Molecule"]
        for field in fields:
            pred_text = pred[field]
            label_text = label[field]
            pred_vec = self.model_encoder.text_encode(pred_text)
            label_vec = self.model_encoder.text_encode(label_text)
            similarity = self.similar_method.compute_similarity(pred_vec, label_vec)
            if similarity < self.threshold:
                return False
        return True


class InfoExtractValidation(BaseValidation):
    """Validates extracted data against ground truth labels and computes metrics."""

    def __init__(self, model_encoder: BaseModelEncode, similar_method: BaseSimilarity, threshold: float = 0.5):
        """Initialize the InfoExtractValidation.

        Args:
            model_encoder: Encoder to convert text to vectors.
            similar_method: Method to compute similarity between vectors.
            threshold: Similarity threshold for matching.
        """
        self.matcher = MatchingProcessor(model_encoder, similar_method, threshold)

    def validate(self, label_json_path: str, predict_json_path: str, save_result: bool = False) -> Dict[str, float]:
        """Validate predictions against ground truth labels and compute metrics.

        Args:
            label_json_path: Path to the JSON file containing ground truth labels.
            predict_json_path: Path to the JSON file containing predicted labels.
            save_result: Whether to save the validation results (not implemented).

        Returns:
            Dictionary containing precision, recall, and f1_score.
        """
        label_data = load_json(label_json_path)
        predict_data = load_json(predict_json_path)

        true_positives, false_positives, matched_labels = self.matcher.match_data(predict_data, label_data)
        false_negatives = len(label_data) - len(matched_labels)

        precision = (
            true_positives / (true_positives + false_positives)
            if (true_positives + false_positives) > 0
            else 0.0
        )
        recall = (
            true_positives / (true_positives + false_negatives)
            if (true_positives + false_negatives) > 0
            else 0.0
        )
        f1_score = (
            2 * (precision * recall) / (precision + recall)
            if (precision + recall) > 0
            else 0.0
        )
        metrics = {
            "precision": precision,
            "recall": recall,
            "f1_score": f1_score,
            "true_positives": true_positives,
            "false_positives": false_positives,
            "false_negatives": false_negatives
        }
        if save_result:
            save_json("results/validation_results.json", metrics)

        return metrics