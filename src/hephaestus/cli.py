from hephaestus.bruno.generator import build_ir
from hephaestus.openapi.loader import load_openapi_spec
import json
from pathlib import Path
import typer


app = typer.Typer(add_completion=False)


@app.command()
def main(path: str) -> None:
    """
    Generate Bruno collection from OpenaAPI spec.
    """
    openapi_spec = load_openapi_spec(path)
    ir = build_ir(openapi_spec)

    typer.echo(f"Collection title: {ir.title}.")
    typer.echo(f"Requests number: {len(ir.requests)}.")

    typer.echo("First 5 requests:")
    for r in ir.requests[:5]:
        typer.echo(f"- {r.method} {r.path} :: {r.name}")
