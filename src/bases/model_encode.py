from abc import ABC, abstractmethod
import numpy as np


class BaseModelEncode(ABC):
    """Abstract base class for encoding text into vectors."""

    @abstractmethod
    def text_encode(self, pdf_text: str) -> np.ndarray:
        """Encode input text into a numerical vector.

        Args:
            pdf_text: Input text to be encoded.

        Returns:
            NumPy array representing the encoded text.

        Examples:
            >>> encoder = SomeEncoderImplementation()
            >>> text = "Sample text"
            >>> encoder.text_encode(text)
            array([0.1, 0.2, 0.3, ...], dtype=float32)
        """
        pass