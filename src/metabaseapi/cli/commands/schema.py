from __future__ import annotations

import typer

from metabaseapi.cli.runtime import _run_and_print
from metabaseapi.cli.runtime import _run_client_call
from metabaseapi.cli.runtime import app
from metabaseapi.client.raw import schema as _raw_schema


@app.command("list-tables")
def list_tables(ctx: typer.Context) -> None:
    """List tables."""

    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: _raw_schema.list_tables(
                client,
            ),
        )
    )


@app.command("get-table")
def get_table(ctx: typer.Context, table_id: str = typer.Argument(...)) -> None:
    """Get a table by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: _raw_schema.get_table(client, table_id)))


@app.command("get-field")
def get_field(ctx: typer.Context, field_id: str = typer.Argument(...)) -> None:
    """Get a field by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: _raw_schema.get_field(client, field_id)))
