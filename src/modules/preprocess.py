import re

from src.bases import BasePreprocessing


class Preprocessing(BasePreprocessing):
    def preprocess(self, text: str) -> str:
        """
        Preprocess the input text by removing unnecessary characters and normalizing whitespace.
        
        :param text: The input text to preprocess.
        :return: Preprocessed text.
        """
        # Remove unnecessary characters and normalize whitespace
        preprocessed_text = re.sub(r'\s+', ' ', text.strip())
        return preprocessed_text