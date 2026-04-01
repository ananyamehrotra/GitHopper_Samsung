import hashlib
from typing import Any, Dict, List


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def build_file_metadata(files: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
    metadata = []
    for file in files:
        content = file.get("content", "")
        metadata.append(
            {
                "path": file["path"],
                "language": file.get("language", "text"),
                "size_bytes": file.get("size_bytes", len(content.encode("utf-8"))),
                "content_hash": sha256_text(content),
                "debt_signal_count": file.get("debt_signal_count", 0),
                "debt_category_hint": file.get("debt_category_hint", "code_quality"),
            }
        )
    return metadata


def compute_incremental_changes(
    current_metadata: List[Dict[str, Any]],
    previous_metadata: List[Dict[str, Any]],
) -> Dict[str, List[str]]:
    current_map = {item["path"]: item for item in current_metadata}
    previous_map = {item["path"]: item for item in previous_metadata}

    new_files = sorted([path for path in current_map if path not in previous_map])
    deleted_files = sorted([path for path in previous_map if path not in current_map])
    modified_files = sorted(
        [
            path for path, item in current_map.items()
            if path in previous_map and item["content_hash"] != previous_map[path]["content_hash"]
        ]
    )
    unchanged_files = sorted(
        [
            path for path, item in current_map.items()
            if path in previous_map and item["content_hash"] == previous_map[path]["content_hash"]
        ]
    )

    return {
        "new_files": new_files,
        "modified_files": modified_files,
        "deleted_files": deleted_files,
        "unchanged_files": unchanged_files,
    }

