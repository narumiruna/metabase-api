from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_client_command
from metabaseapi.client.raw import table as _raw_table


@app.command("list-tables")
def list_tables(ctx: typer.Context) -> None:
    """List tables."""

    run_client_command(
        ctx,
        lambda client: _raw_table.list_tables(
            client,
        ),
    )


@app.command("get-table")
def get_table(ctx: typer.Context, table_id: str = typer.Argument(...)) -> None:
    """Get a table by ID."""

    run_client_command(ctx, lambda client: _raw_table.get_table(client, table_id))
