from abc import ABC, abstractmethod


class BaseValidation(ABC):
    """Abstract base class for validating predictions against ground truth."""

    @abstractmethod
    def validate(self, label_json_path: str, predict_json_path: str, save_result: bool = True) -> dict:
        """Validate predictions against ground truth labels.

        Args:
            label_json_path: Path to the JSON file with ground truth labels.
            predict_json_path: Path to the JSON file with predicted labels.
            save_result: Whether to save the validation results (default: True).

        Returns:
            Dictionary containing validation metrics (e.g., precision, recall).

        Examples:
            >>> validator = SomeValidationImplementation()
            >>> label_path = "labels.json"
            >>> predict_path = "predictions.json"
            >>> validator.validate(label_path, predict_path, save_result=False)
            {'precision': 0.9, 'recall': 0.85, 'f1_score': 0.87}
        """
        pass