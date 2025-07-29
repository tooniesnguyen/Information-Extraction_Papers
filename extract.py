import os
from dotenv import load_dotenv

from src.modules.schema import CompoundList
from src.modules.gemini_extract import GeminiExtract
from src.modules.pdf_ingest import PDFIngestion
from src.modules.preprocess import Preprocessing
from src.modules.chunking import RecursiveChunking
from src.modules.prompt import GeminiPrompt

from src.services.info_extract import InforExtraction

from src.utils.reader import load_yaml

def main():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    
    config = load_yaml("configs/extract.yaml")
    
    llm_extract = GeminiExtract(
        model_name=config['llms_extract']['model_name'],
        schema=CompoundList,
        api_key=api_key,
        max_attempts=config['llms_extract']['max_attempts'],
        time_delay=config['llms_extract']['time_delay']
        )
    pdf_ingest = PDFIngestion()
    preprocessing = Preprocessing()
    chunking = RecursiveChunking(chunk_size=config["chunk"]["size"], 
                                 chunk_overlap=config["chunk"]["overlap"])
    prompt = GeminiPrompt()
    
    info_extraction = InforExtraction(
        llm_extract=llm_extract,
        pdf_ingestion=pdf_ingest,
        preprocessing=preprocessing,
        chunking=chunking,
        prompting=prompt
    )
    
    pdf_path = "data/labeled/paper1.pdf"
    extracted_data = info_extraction.extract_info(pdf_path, visualize=True)
    print(extracted_data)
    

if __name__ == "__main__":
    main()