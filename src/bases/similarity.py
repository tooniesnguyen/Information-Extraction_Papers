from abc import ABC, abstractmethod
import numpy as np


class BaseSimilarity(ABC):
    """Abstract base class for similarity computation between vectors."""

    @abstractmethod
    def compute_similarity(self, vector1: np.ndarray, vector2: np.ndarray) -> float:
        """Compute similarity between two vectors.

        Args:
            vector1: First input vector as a NumPy array.
            vector2: Second input vector as a NumPy array.

        Returns:
            Similarity score as a float.
        """
        pass
