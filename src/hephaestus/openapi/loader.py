"""OpenAPI specification loader.

Responsible for reading and parsing OpenAPI JSON files into Python dictionaries.
"""

import json
from pathlib import Path


def load_openapi_spec(path: str) -> dict:
    """Load an OpenAPI JSON file from disk.

    Args:
        path: Path to OpenAPI JSON file.

    Returns:
        Parsed OpenAPI specification as dictionary.

    Raises:
        FileNotFoundError: If the file does not exist.
        json.JSONDecodeError: If the file is not valid JSON.
    """
    file_path = Path(path)

    if not file_path.exists():
        msg = f"OpenAPI file not found: {path}."
        raise FileNotFoundError(msg)

    return json.loads(file_path.read_text())
