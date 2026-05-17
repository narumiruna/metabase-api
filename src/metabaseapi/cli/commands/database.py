from __future__ import annotations

import typer

from metabaseapi.cli.runtime import _parse_json_body
from metabaseapi.cli.runtime import _run_and_print
from metabaseapi.cli.runtime import _run_client_call
from metabaseapi.cli.runtime import app


@app.command("list-databases")
def list_databases(ctx: typer.Context) -> None:
    """List configured databases."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_databases()))


@app.command("get-database")
def get_database(ctx: typer.Context, database_id: str = typer.Argument(...)) -> None:
    """Get a database by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_database(database_id)))


@app.command("create-database")
def create_database(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Name of the database to create"),
    engine: str = typer.Argument(..., help="Database engine type"),
    details: str | None = typer.Option(None, "--details", "-d", help="Database details JSON object"),
) -> None:
    """Create a new database."""

    details_payload: dict[str, object] | None
    if details is None:
        details_payload = None
    else:
        parsed = _parse_json_body(details)
        if parsed is not None and not isinstance(parsed, dict):
            raise typer.BadParameter("details must be a JSON object")
        details_payload = parsed

    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.create_database(name=name, engine=engine, details=details_payload),
        ),
    )
