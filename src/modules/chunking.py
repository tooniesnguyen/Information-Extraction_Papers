from langchain.text_splitter import RecursiveCharacterTextSplitter
from src.bases import BaseChunking

class RecursiveChunking(BaseChunking):
    def __init__(self, chunk_size=100, chunk_overlap=20):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len
        )

    def chunk(self, text: str) -> list[str]:
        return self.text_splitter.split_text(text)