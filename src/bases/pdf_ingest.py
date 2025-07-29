from abc import ABC, abstractmethod


class BasePDFIngestion(ABC):
    """Abstract base class for extracting text from PDF files."""

    @abstractmethod
    def extract(self, pdf_path: str) -> str:
        """Extract text from a PDF file.

        Args:
            pdf_path: Path to the PDF file.

        Returns:
            Extracted text as a string.

        Examples:
            >>> pdf_ingestor = SomePDFIngestorImplementation()
            >>> pdf_path = "sample.pdf"
            >>> pdf_ingestor.extract(pdf_path)
            'This is the extracted text from the PDF.'
        """
        pass