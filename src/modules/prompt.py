from typing import List

from src.bases import BaseLLMsPrompt


QUERY = """
    You are an expert assistant tasked with extracting structured information from a scientific paper discussing plant-derived compounds. Read the provided text and extract the following information from schemas provided:
    If multiple compounds are mentioned, return a list of compounds. If no compounds are found, return an empty list. Ensure the output is structured as a JSON list of objects, each with the fields above.

    Here is the text from the paper:
    {pdf_text}
    """
    

class GeminiPrompt(BaseLLMsPrompt):
    def __init__(self) -> None:
        self.query = QUERY

    def create_messages(self, chunked_text: str) -> List[dict]:

        message = [{
                "role": "user",
                "content": self.query.format(pdf_text=chunked_text)
            }]
        return message