from typing import List

from src.bases import BaseLLMsPrompt


QUERY = """
    You are an information extraction system designed to parse biochemical data from scientific articles. Your goal is to extract structured information about each biomolecule mentioned in the text.


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