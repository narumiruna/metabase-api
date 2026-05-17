from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.notify import NotifyAttachedDatawarehouseRequest
from metabaseapi.endpoints.requests.notify import NotifyDatabaseNewTableRequest
from metabaseapi.endpoints.requests.notify import NotifyDatabaseRequest


@app.command("notify-attached-datawarehouse")
def notify_attached_datawarehouse(
    ctx: typer.Context,
    body: str = typer.Argument("{}", help="Attached datawarehouse notification JSON object"),
) -> None:
    """Notify Metabase about an attached data warehouse change."""

    run_json_body_endpoint_command(ctx, body, lambda payload: NotifyAttachedDatawarehouseRequest(body=payload))


@app.command("notify-database")
def notify_database(
    ctx: typer.Context,
    database_id: str = typer.Argument(..., help="Database ID"),
    body: str = typer.Argument("{}", help="Database notification JSON object"),
) -> None:
    """Notify Metabase about a database schema change."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: NotifyDatabaseRequest(database_id=database_id, body=payload),
    )


@app.command("notify-database-new-table")
def notify_database_new_table(
    ctx: typer.Context,
    database_id: str = typer.Argument(..., help="Database ID"),
    body: str = typer.Argument(..., help="New table notification JSON object"),
) -> None:
    """Notify Metabase about a new database table."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: NotifyDatabaseNewTableRequest(database_id=database_id, body=payload),
    )
