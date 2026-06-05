"""Lightweight OpenAPI $ref resolver.

Resolves internal references like:
#/components/schemas/XYZ
"""

from typing import Any


def resolve_ref(spec: dict, ref: str) -> Any:
    """Resolve ref."""
    if not ref.startswith("#/"):
        return None

    parts = ref.lstrip("#/").split("/")
    current = spec

    for part in parts:
        if not isinstance(current, dict):
            return None
        current = current.get(part)

    return current
