from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True, kw_only=True)
class Request:
    name: str
    method: str
    path: str
    params: dict[str, Any]
    headers: dict[str, str]
    body: Any | None


@dataclass(frozen=True, slots=True, kw_only=True)
class Collection:
    title: str
    requests: list[Request]
