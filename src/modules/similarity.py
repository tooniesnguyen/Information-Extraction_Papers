import numpy as np

from src.bases import BaseSimilarity

class CosineSimilarity(BaseSimilarity):
    """Class to compute cosine similarity between two vectors."""

    def compute_similarity(self, vector1: np.ndarray, vector2: np.ndarray) -> float:
        """Calculate the cosine similarity between two vectors.

        Args:
            vector1: First input vector as a NumPy array.
            vector2: Second input vector as a NumPy array.

        Returns:
            Cosine similarity as a float. Returns 0.0 if either vector has zero norm.
        """
        norm1 = np.linalg.norm(vector1)
        norm2 = np.linalg.norm(vector2)
        if norm1 == 0 or norm2 == 0:
            return 0.0
        return np.dot(vector1, vector2) / (norm1 * norm2)