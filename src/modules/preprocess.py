import re

from src.bases import BasePreprocessing


class Preprocessing(BasePreprocessing):
    def preprocess(self, text: str) -> str:
        
        # Remove unnecessary characters and normalize whitespace
        preprocessed_text = re.sub(r'\s+', ' ', text.strip())
        return preprocessed_text