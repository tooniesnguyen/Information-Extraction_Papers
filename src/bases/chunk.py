from abc import ABC, abstractmethod
from typing import List


class BaseChunking(ABC):
    """Abstract base class for chunking text data."""

    @abstractmethod
    def chunk(self, pdf_text: str) -> List[str]:
        """Chunk input text into smaller segments.

        Args:
            pdf_text: Input text to be chunked.

        Returns:
            List of text chunks.

        Examples:
            >>> chunker = SomeChunkerImplementation()
            >>> text = "This is a sample text. It will be split into chunks."
            >>> chunker.chunk(text)
            ['This is a sample text.', 'It will be split into chunks.']
        """
        pass