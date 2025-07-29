from abc import ABC, abstractmethod
from typing import List, Dict, Type
from pydantic import BaseModel


class BasePosProcessing(ABC):
    """Abstract base class for post-processing text data."""

    @abstractmethod
    def process(self, text: str) -> str:
        """Process input text to clean or transform it.

        Args:
            text: Input text to be processed.

        Returns:
            Processed text as a string.

        Examples:
            >>> processor = SomePostProcessorImplementation()
            >>> text = "  Raw text   with  extra  spaces.  "
            >>> processor.process(text)
            'Raw text with extra spaces.'
        """
        pass