from langchain.text_splitter import RecursiveCharacterTextSplitter
from src.bases import BaseChunking

class RecursiveChunking(BaseChunking):
    def __init__(self, chunk_size=100, chunk_overlap=20):
        """
        Khởi tạo lớp Chunking với các tham số chunk_size và chunk_overlap.
        
        Args:
            chunk_size (int): Kích thước tối đa của mỗi chunk (tính bằng ký tự).
            chunk_overlap (int): Số ký tự chồng lấn giữa các chunk để duy trì ngữ cảnh.
        """
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len
        )

    def chunk(self, text: str) -> list[str]:
        """
        Chia nhỏ văn bản thành các chunk sử dụng LangChain's RecursiveCharacterTextSplitter.
        
        Args:
            text (str): Văn bản đầu vào cần chia nhỏ.
        
        Returns:
            list[str]: Danh sách các chunk văn bản.
        """
        return self.text_splitter.split_text(text)