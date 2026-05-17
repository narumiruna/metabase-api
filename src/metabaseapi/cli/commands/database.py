from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.database import CreateDatabaseRequest
from metabaseapi.endpoints.requests.database import GetDatabaseRequest
from metabaseapi.endpoints.requests.database import ListDatabasesRequest


@app.command("list-databases")
def list_databases(ctx: typer.Context) -> None:
    """List configured databases."""

    run_endpoint_command(ctx, ListDatabasesRequest())


@app.command("get-database")
def get_database(ctx: typer.Context, database_id: str = typer.Argument(...)) -> None:
    """Get a database by ID."""

    run_endpoint_command(ctx, GetDatabaseRequest(database_id=database_id))


@app.command("create-database")
def create_database(
    ctx: typer.Context,
    name: str = typer.Argument(..., help="Name of the database to create"),
    engine: str = typer.Argument(..., help="Database engine type"),
    details: str | None = typer.Option(None, "--details", "-d", help="Database details JSON object"),
) -> None:
    """Create a new database."""

    run_endpoint_command(
        ctx,
        CreateDatabaseRequest(name=name, engine=engine, details=parse_optional_json_object(details, "details") or {}),
    )
