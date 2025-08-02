import json
from pathlib import Path


def parse_time_range(time_range: str):
    """Split a time range string like '08:00-12:00' into start and end."""
    start, end = time_range.split("-")
    return start.strip(), end.strip()


def load_json(path: Path):
    """Load JSON data from a file path."""
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(data, path: Path):
    """Save JSON data to a file path."""
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
