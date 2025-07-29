from pydantic import BaseModel

from src.bases import BasePDFIngestion
from src.bases import BasePreprocessing
from src.bases import BaseChunking
from src.bases import BaseLLMsPrompt
from src.bases import BaseLLMsExtract
from src.bases import BasePosProcessing

from src.utils.writer import save_json
from src.utils.timer import time_complexity

class InforExtraction:
    def __init__(self, 
                 pdf_ingestion: BasePDFIngestion,
                 preprocessing: BasePreprocessing,
                 chunking: BaseChunking,
                 prompting: BaseLLMsPrompt,
                 llm_extract: BaseLLMsExtract,
                #  pos_processing: BasePosProcessing,
                ) -> None:
        
        self.pdf_ingestion = pdf_ingestion
        self.preprocessing = preprocessing
        self.chunking  = chunking
        self.prompting = prompting
        self.llm_extract = llm_extract
        # self.pos_processing = pos_processing
        
    
    @time_complexity(name_process="Extracting information from PDF")
    def extract_info(self, pdf_path: str, visualize: bool = False) -> dict:
        """
        Extract information using the LLM client based on the provided messages.
        
        :param messages: List of messages to send to the LLM.
        :return: Extracted information as a dictionary.
        """
        pdf_text = self.pdf_ingestion.extract(pdf_path)
        preprocess_text = self.preprocessing.preprocess(pdf_text)
        list_chunked_text = self.chunking.chunk(preprocess_text)
        
        responses = []
        for chunked_text in list_chunked_text:
            messages = self.prompting.create_messages(chunked_text)
            response = self.llm_extract.get_response(messages)
            responses.extend(response)
            
        if visualize:
            save_json("results/extracted_info.json", responses)
            
        return responses