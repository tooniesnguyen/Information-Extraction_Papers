from typing import List, Dict
from pathlib import Path


def save_json(file_path: str, content: List[Dict]) -> None:
    import json
    """
    Lưu nội dung danh sách các dictionary vào file JSON.

    Args:
        file_path (str): Đường dẫn đến file JSON cần lưu.
        content (List[Dict]): Danh sách các dictionary cần lưu.
    """
    output_path = Path(file_path)
    output_path.parent.mkdir(exist_ok=True)  # Tạo thư mục cha nếu chưa tồn tại
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(content, f, indent=2, ensure_ascii=False)