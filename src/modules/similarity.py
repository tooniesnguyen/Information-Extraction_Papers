import numpy as np

from src.bases import BaseSimilarity

class CosineSimilarity(BaseSimilarity):
    def compute_similarity(self, vector1: np.ndarray, vector2: np.ndarray) -> float:

        norm1 = np.linalg.norm(vector1)
        norm2 = np.linalg.norm(vector2)
        if norm1 == 0 or norm2 == 0:
            return 0.0
        return np.dot(vector1, vector2) / (norm1 * norm2)