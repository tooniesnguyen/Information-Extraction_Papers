import argparse
from src.modules.model_encode import TransformerEncode
from src.modules.similarity import CosineSimilarity
from src.modules.validation import InfoExtractValidation

def main():
    parser = argparse.ArgumentParser(description="Validate extracted information against labeled data.")
    parser.add_argument(
        "--label_json_path",
        type=str,
        default="data/labeled/paper1.json",
        help="Path to the labeled JSON file."
    )
    parser.add_argument(
        "--predict_json_path",
        type=str,
        default="results/extracted_info.json",
        help="Path to the predicted JSON file."
    )
    args = parser.parse_args()

    model_encoder = TransformerEncode(model_name='sentence-transformers/all-MiniLM-L6-v2', device="cuda")
    similar_method = CosineSimilarity()
    validation = InfoExtractValidation(
        model_encoder=model_encoder,
        similar_method=similar_method,
        threshold=0.7
    )
    
    results = validation.validate(
        label_json_path=args.label_json_path,
        predict_json_path=args.predict_json_path,
        save_result=True
    )
    print("Validation Results:", results)

if __name__ == "__main__":
    main()