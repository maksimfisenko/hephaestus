"""Filesystem writer for Bruno collections.

Responsible for converting IR into Bruno-compatible folder and file structure.
"""

import json
from pathlib import Path
from textwrap import dedent
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from hephaestus.ir.models import Collection, Request


def sanitize_name(name: str) -> str:
    """Sanitize a string for safe filesystem usage."""
    return "".join(c for c in name if c.isalnum() or c in (" ", "-", "_")).strip()


def request_to_bru(req: Request) -> str:
    """Convert a RequestIR into a Bruno `.bru` file format."""
    return dedent(f"""
        meta {{
            name: {req.name}
            type: http
        }}

        http {{
            method: {req.method}
            url: {{baseUrl}}{req.path}
        }}
    """)


def write_collection(ir: Collection, output_dir: str) -> Path:
    """Write a Bruno collection to disk.

    Args:
        ir: Internal representation of the collection.
        output_dir: Target output directory.

    Returns:
        Path to generated collection root.
    """
    root = Path(output_dir) / sanitize_name(ir.title)
    root.mkdir(parents=True, exist_ok=True)

    (root / "bruno.json").write_text(
        json.dumps(
            {
                "name": ir.title,
                "type": "collection",
            },
            indent=2,
        ),
    )

    for req in ir.requests:
        filename = sanitize_name(req.name) + ".bru"
        (root / filename).write_text(request_to_bru(req))

    return root
