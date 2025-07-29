# Information Extraction and Validation System

This project provides a modular system for extracting structured information from scientific PDFs and validating the results against labeled data. The system is organized into two main scripts: `extract.py` for extraction and `valid.py` for validation.

## Prerequisites
- **Python**: 3.10+
- **Dependencies**: Install required packages using:
  ```bash
  pip install -r requirements.txt
  ```
- **Environment**: Set up a `.env` file with your Google API key:
  ```plaintext
  GOOGLE_API_KEY=your_api_key_here
  ```
- **Configuration**: Ensure `configs/extract.yaml` exists with settings for the extraction pipeline (e.g., model name, chunk size, retry settings).
- **Hardware**: For `valid.py`, a CUDA-capable GPU is recommended for the `TransformerEncode` model, but CPU fallback is supported.

## Directory Structure
- `src/bases/`: Base classes defining interfaces for modules.
- `src/modules/`: Functional modules (e.g., PDF ingestion, text chunking, Gemini extraction, validation).
- `src/services/`: Pipeline orchestration (e.g., `info_extract.py`).
- `src/utils/`: Helper utilities (e.g., logging, file I/O).
- `configs/`: Configuration files (e.g., `extract.yaml`).
- `data/labeled/`: Labeled data for validation (e.g., `paper1.json`).
- `results/`: Output directory for extracted data (e.g., `extracted_info.json`).

## 1. Extraction (`extract.py`)
### Purpose
Extracts structured information (e.g., compounds, plant species, quantities) from a PDF using the Gemini API and a modular pipeline.

### Usage
Run the extraction script with a specified PDF path:
```bash
python extract.py --pdf_path /path/to/your/paper.pdf
```

- **Default Path**: If no `--pdf_path` is provided, it uses `data/labeled/paper1.pdf`.
- **Options**:
  - `--pdf_path`: Path to the input PDF file.
- **Example**:
  ```bash
  python extract.py --pdf_path data/labeled/paper2.pdf
  ```

### Input
- A PDF file containing scientific text (e.g., a research paper).
- A `configs/extract.yaml` file specifying:
  - `llms_extract.model_name`: Gemini model (e.g., `gemini-1.5-flash`).
  - `llms_extract.max_attempts`: Max API retry attempts.
  - `llms_extract.time_delay`: Initial delay for retries.
  - `chunk.size`: Maximum chunk size for text splitting.
  - `chunk.overlap`: Overlap between text chunks.

### Output
- Prints extracted data (JSON format) to the console, structured as a `CompoundList` (defined in `src/modules/schema.py`).
- Example output:
  ```json
  {
    "compounds": [
      {
        "Name": "Caffeine",
        "Species": "Coffea arabica",
        "Plant_Part": "seeds",
        "Organisms": "12.5 mg/kg",
      }
    ]
  }
  ```
- Optionally saves results to a file (configured in `info_extract.py`).

## 2. Validation (`valid.py`)
### Purpose
Validates extracted information against labeled data using a transformer-based encoder and cosine similarity, producing metrics.

### Usage
Run the validation script with specified JSON paths:
```bash
python valid.py --label_json_path /path/to/labels.json --predict_json_path /path/to/predictions.json
```

- **Default Paths**:
  - `--label_json_path`: `data/labeled/paper1.json`
  - `--predict_json_path`: `results/extracted_info.json`
- **Example**:
  ```bash
  python valid.py --label_json_path data/labeled/paper1.json --predict_json_path results/extracted_info.json
  ```

### Input
- **Labeled JSON**: Ground truth data (e.g., `paper1.json`) with the same structure as `CompoundList`.
- **Predicted JSON**: Extracted data (e.g., `extracted_info.json`) from `extract.py`.
- A transformer model (`sentence-transformers/all-MiniLM-L6-v2`) for encoding text to compute similarity.

### Output
- Prints validation results (e.g., accuracy, precision, recall, or similarity scores) to the console.
- Example output:
  ```json
  {
    "accuracy": 0.85,
    "precision": 0.90,
    "recall": 0.80,
    "low_confidence_compounds": [...]
  }
  ```
- Saves results to a file if `save_result=True` (configured in `valid.py`).

## Running the Full Pipeline
1. **Extract**:
   ```bash
   python extract.py --pdf_path data/labeled/paper1.pdf
   ```
   This generates `results/extracted_info.json`.
2. **Validate**:
   ```bash
   python valid.py --label_json_path data/labeled/paper1.json --predict_json_path results/extracted_info.json
   ```

## Notes
- Ensure all paths (`pdf_path`, `label_json_path`, `predict_json_path`) are valid and accessible.
- Check `configs/extract.yaml` for correct settings.
- For GPU usage in `valid.py`, ensure CUDA is installed; otherwise, it falls back to CPU.
- If errors occur, check logs in `src/utils/logger.py` output or console for debugging.