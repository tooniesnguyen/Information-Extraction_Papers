from abc import ABC, abstractmethod
from typing import List, Dict, Type
from pydantic import BaseModel


class BasePreprocessing(ABC):
    """Abstract base class for preprocessing text data."""

    @abstractmethod
    def preprocess(self, pdf_text: str) -> str:
        """Preprocess input text to prepare it for further processing.

        Args:
            pdf_text: Input text to be preprocessed.

        Returns:
            Preprocessed text as a string.

        Examples:
            >>> preprocessor = SomePreprocessorImplementation()
            >>> text = "Raw   TEXT  with\\nextra spaces!"
            >>> preprocessor.preprocess(text)
            'raw text with extra spaces'
        """
        pass