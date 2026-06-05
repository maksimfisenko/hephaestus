"""Transforms OpenAPI specification into internal representation (IR)."""

from hephaestus.ir.models import Collection, Request


def build_ir(openapi_spec: dict) -> Collection:
    """Convert OpenAPI spec into internal representation (IR).

    Args:
        openapi_spec: Parsed OpenAPI JSON object.

    Returns:
        Collection representing normalized API structure.
    """
    info = openapi_spec.get("info", {})
    paths = openapi_spec.get("paths", {})

    requests: list[Request] = []

    for path, methods in paths.items():
        for method, spec in methods.items():
            params = spec.get("parameters", [])

            path_params = {}
            query_params = {}
            headers = {}

            for p in params:
                location = p.get("in")
                name = p.get("name")

                if location == "path":
                    path_params[name] = p
                elif location == "query":
                    query_params[name] = p
                elif location == "header":
                    headers[name] = p

            body = spec.get("requestBody")

            requests.append(
                Request(
                    name=spec.get("summary", f"{method.upper()} {path}"),
                    method=method.upper(),
                    path=path,
                    path_params=path_params,
                    query_params=query_params,
                    headers=headers,
                    body=body,
                )
            )

    return Collection(
        title=info.get("title", "Untitled"),
        requests=requests,
    )
