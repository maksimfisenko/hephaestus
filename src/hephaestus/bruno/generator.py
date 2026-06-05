from hephaestus.ir.models import Collection, Request


def build_ir(openapi_spec: dict) -> Collection:
    info = openapi_spec.get("info", {})
    paths = openapi_spec.get("paths", {})

    requests: list[Request] = []

    for path, methods in paths.items():
        for method, spec in methods.items():
            requests.append(
                Request(
                    name=spec.get("summary", f"{method.upper()} {path}"),
                    method=method.upper(),
                    path=path,
                    params={},
                    headers={},
                    body=None,
                )
            )

    return Collection(
        title=info.get("title", "Untitled"),
        requests=requests,
    )
