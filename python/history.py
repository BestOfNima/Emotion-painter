import json
import os
from datetime import datetime

HISTORY_FOLDER = "json"
HISTORY_FILE = os.path.join(HISTORY_FOLDER, "history.json")


def _ensure_folder():
    os.makedirs(HISTORY_FOLDER, exist_ok=True)


def load_history() -> list:
    """
    Load the stored (prompt, image_path) history.

    Tolerant of a missing or corrupted file - always returns a list.
    """

    _ensure_folder()

    if not os.path.exists(HISTORY_FILE):
        return []

    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, list):
            return data

        return []

    except Exception:
        return []


def add_entry(prompt: str, image_path: str) -> list:
    """
    Append a new {prompt, image_path, timestamp} entry to the history
    JSON file and return the updated history.
    """

    _ensure_folder()

    history = load_history()

    history.append({
        "prompt": prompt,
        "image_path": image_path,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    })

    with open(HISTORY_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=2)

    return history
