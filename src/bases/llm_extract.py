from abc import ABC, abstractmethod
from typing import List, Dict, Type
from pydantic import BaseModel


class BaseLLMsExtract(ABC):
    """Abstract base class for extracting data using LLMs."""

    @abstractmethod
    def get_response(self, messages: List[Dict]) -> List[Dict]:
        """Generate a response from a language model based on input messages.

        Args:
            messages: List of message dictionaries for the model.

        Returns:
            Dictionary containing the model's response.

        Examples:
            >>> llm = SomeLLMImplementation()
            >>> messages = [{"role": "user", "content": "Extract data from this text."}]
            >>> llm.get_response(messages)
            {'key 1': 'Extracted data', 'key 2': '...'}
        """
        pass