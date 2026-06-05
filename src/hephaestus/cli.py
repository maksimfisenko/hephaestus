"""Hephaestus CLI entrypoint.

This module exposes the command-line interface for converting an OpenAPI
specification into a Bruno API collection.

The CLI orchestrates the full pipeline:
    OpenAPI JSON → IR → Bruno filesystem output
"""

import typer

from hephaestus.bruno.generator import build_ir
from hephaestus.bruno.writer import write_collection
from hephaestus.openapi.loader import load_openapi_spec


app = typer.Typer(add_completion=False)


@app.command()
def main(path: str, out: str) -> None:
    """Generate a Bruno collection from an OpenAPI specification.

    Args:
        path: Path to OpenAPI JSON file.
        out: Output directory for generated Bruno collection.

    Workflow:
        1. Load OpenAPI spec from file
        2. Convert to internal representation (IR)
        3. Write Bruno collection to filesystem
    """
    openapi_spec = load_openapi_spec(path)
    ir = build_ir(openapi_spec)
    output_path = write_collection(ir, out)

    typer.echo(f"Generated Bruno collection at: {output_path}.")
    typer.echo(f"Collection: {ir.title}.")
    typer.echo(f"Requests: {len(ir.requests)}.")
