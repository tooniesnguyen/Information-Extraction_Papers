

from src.modules.model_encode import TransformerEncode
from src.modules.similarity import CosineSimilarity
from src.modules.validation import InfoExtractValidation




def main():
    model_encoder = TransformerEncode(model_name='sentence-transformers/all-MiniLM-L6-v2', device = "cuda")
    similar_method = CosineSimilarity()
    validation = InfoExtractValidation(model_encoder=model_encoder, similar_method=similar_method, threshold=0.7)
    
    label_json_path = 'data/labeled/paper1.json'
    predict_json_path = 'results/extracted_info.json'
    results = validation.validate(label_json_path=label_json_path, predict_json_path=predict_json_path, save_result=True)
    print("Validation Results:", results)
    
if __name__ == "__main__":
    main()