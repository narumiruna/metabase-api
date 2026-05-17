from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_json_body
from metabaseapi.cli.runtime import run_client_command
from metabaseapi.client.raw import database as _raw_database


@app.command("list-databases")
def list_databases(ctx: typer.Context) -> None:
    """List configured databases."""

    run_client_command(
        ctx,
        lambda client: _raw_database.list_databases(
            client,
        ),
    )


@app.command("get-database")
def get_database(ctx: typer.Context, database_id: str = typer.Argument(...)) -> None:
    """Get a database by ID."""

    run_client_command(ctx, lambda client: _raw_database.get_database(client, database_id))


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
        parsed = parse_json_body(details)
        if parsed is not None and not isinstance(parsed, dict):
            raise typer.BadParameter("details must be a JSON object")
        details_payload = parsed

    run_client_command(
        ctx,
        lambda client: _raw_database.create_database(client, name=name, engine=engine, details=details_payload),
    )
