import json
from pathlib import Path


def load_openapi_spec(path: str) -> dict:
    file_path = Path(path)

    if not file_path.exists():
        raise FileNotFoundError(f"OpenAPI file not found: {path}.")

    return json.loads(file_path.read_text())
