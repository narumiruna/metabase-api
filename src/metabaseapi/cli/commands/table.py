from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.table import GetTableRequest
from metabaseapi.endpoints.requests.table import ListTablesRequest


@app.command("list-tables")
def list_tables(ctx: typer.Context) -> None:
    """List tables."""

    run_endpoint_command(ctx, ListTablesRequest())


@app.command("get-table")
def get_table(ctx: typer.Context, table_id: str = typer.Argument(...)) -> None:
    """Get a table by ID."""

    run_endpoint_command(ctx, GetTableRequest(table_id=table_id))
