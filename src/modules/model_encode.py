from typing import Union
import numpy as np
from sentence_transformers import SentenceTransformer
from src.bases.model_encode import BaseModelEncode

class TransformerEncode(BaseModelEncode):
    def __init__(self, model_name: str = 'sentence-transformers/all-MiniLM-L6-v2', 
                 device: str = 'cpu'):
        self.model = SentenceTransformer(model_name, device=device)

    def text_encode(self, pdf_text: str) -> np.ndarray:
        return self.model.encode(pdf_text.lower().strip())