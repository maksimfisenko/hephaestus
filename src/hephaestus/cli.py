import json
from pathlib import Path
import typer


app = typer.Typer(add_completion=False)


@app.command()
def main(path: str) -> None:
    """
    Generate Bruno collection from OpenaAPI spec.
    """
    file_path = Path(path)

    if not file_path.exists():
        typer.echo(f"File not found: {file_path}.")
        raise typer.Exit(1)

    try:
        data = json.loads(file_path.read_text())
    except json.JSONDecodeError as e:
        typer.echo(f"Invalid JSON: {e}.")
        raise typer.Exit(1)

    typer.echo("OpenAPI spec loaded successfully.")
    typer.echo(f"Title: {data.get('info', {}).get('title', 'unknown')}.")
    typer.echo(f"Paths: {len(data.get('paths', {}))}.")
