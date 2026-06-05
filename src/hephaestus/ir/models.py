"""Data models for Hephaestus Internal Representation (IR).

These structures represent a normalized API description independent
of OpenAPI and Bruno formats.
"""

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True, kw_only=True)
class Request:
    """Internal representation of a single HTTP request."""

    name: str
    method: str
    path: str

    path_params: dict[str, Any]
    query_params: dict[str, Any]
    headers: dict[str, str]
    body: Any | None


@dataclass(frozen=True, slots=True, kw_only=True)
class Collection:
    """Internal representation of a full API collection."""

    title: str
    requests: list[Request]
