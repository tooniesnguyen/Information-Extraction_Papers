import pdfplumber

from src.bases import BasePDFIngestion

class PDFIngestion(BasePDFIngestion):
    def extract(self, pdf_path: str) -> str:
        """
        Ingest a PDF file and extract its text content.
        
        :param pdf_path: Path to the PDF file.
        :return: Extracted text from the PDF.
        """
        with pdfplumber.open(pdf_path) as pdf:
            text = ""
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
            return text
       