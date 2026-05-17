from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object_or_empty
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.database import CreateDatabaseRequest
from metabaseapi.endpoints.requests.database import CreateSampleDatabaseRequest
from metabaseapi.endpoints.requests.database import DeleteDatabaseRequest
from metabaseapi.endpoints.requests.database import GetDatabaseRequest
from metabaseapi.endpoints.requests.database import ListDatabasesRequest
from metabaseapi.endpoints.requests.database import UpdateDatabaseRequest
from metabaseapi.endpoints.requests.database import ValidateDatabaseRequest


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
        CreateDatabaseRequest(
            name=name,
            engine=engine,
            details=parse_optional_json_object_or_empty(details, "details"),
        ),
    )


@app.command("create-sample-database")
def create_sample_database(ctx: typer.Context) -> None:
    """Create Metabase's sample database."""

    run_endpoint_command(ctx, CreateSampleDatabaseRequest())


@app.command("validate-database")
def validate_database(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Database validation JSON object"),
) -> None:
    """Validate database connection details."""

    run_json_body_endpoint_command(ctx, body, lambda payload: ValidateDatabaseRequest(body=payload))


@app.command("update-database")
def update_database(
    ctx: typer.Context,
    database_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Database update JSON object"),
) -> None:
    """Update a database."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: UpdateDatabaseRequest(database_id=database_id, body=payload),
    )


@app.command("delete-database")
def delete_database(ctx: typer.Context, database_id: str = typer.Argument(...)) -> None:
    """Delete a database."""

    run_endpoint_command(ctx, DeleteDatabaseRequest(database_id=database_id))
