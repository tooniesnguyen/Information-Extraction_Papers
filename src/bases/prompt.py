from abc import ABC, abstractmethod
from typing import List, Dict

class BaseLLMsPrompt(ABC):
    """Abstract base class for creating messages for language models."""

    @abstractmethod
    def create_messages(self, pdf_text: str) -> List[Dict]:
        """Create messages for a language model from input text.

        Args:
            pdf_text: Input text to be formatted into messages.

        Returns:
            List of dictionaries representing messages for the language model.

        Examples:
            >>> prompt = SomePromptImplementation()
            >>> text = "Sample text about plant compounds."
            >>> prompt.create_messages(text)
            [{"role": "user", "content": "Extract compounds from: Sample text about plant compounds."}]
        """
        pass
