import time
import json

from pydantic import BaseModel
from langchain_google_genai import ChatGoogleGenerativeAI

from src.bases import BaseLLMsExtract


class GeminiExtract(BaseLLMsExtract):
    def __init__(self, model_name: str, 
                 schema:  BaseModel, 
                 api_key: str,
                 max_attempts: int,
                 time_delay: int = 2
                 ):
        
        self.structured_llm = ChatGoogleGenerativeAI(
            model=model_name,
            temperature=0,
            max_tokens=None,
            timeout=None,
            max_retries=2,
            api_key=api_key
        ).with_structured_output(schema)
        
        self.max_attempts = max_attempts
        self.time_delay = time_delay

    def get_response(self, messages: list) -> list:
        result = self._invoker_with_retry(messages)
        result_dict = result.dict() 
        first_value = next(iter(result_dict.values()))
        return first_value
    
    def _invoker_with_retry(self, messages: list):
        """Gọi API với cơ chế thử lại khi gặp lỗi 429."""
        
        for attempt in range(self.max_attempts):
            try:
                return self.structured_llm.invoke(messages)
            except Exception as e:
                if "429" in str(e) and attempt < self.max_attempts - 1:
                    delay = self.time_delay * (2 ** attempt)
                    print(f"Retrying in {delay} seconds due to 429 error...")
                    time.sleep(delay)
                else:
                    raise e
        raise Exception("Max retries exceeded")