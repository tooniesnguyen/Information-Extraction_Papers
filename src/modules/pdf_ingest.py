import pdfplumber

from src.bases import BasePDFIngestion

class PDFIngestion(BasePDFIngestion):
    def extract(self, pdf_path: str) -> str:
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            return text
       