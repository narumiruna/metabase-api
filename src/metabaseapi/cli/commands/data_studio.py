from __future__ import annotations

import typer

from metabaseapi.cli.runtime import _parse_json_object
from metabaseapi.cli.runtime import _run_and_print
from metabaseapi.cli.runtime import _run_client_call
from metabaseapi.cli.runtime import app


@app.command("data-studio-table-discard-values")
def data_studio_table_discard_values(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Data Studio table selection JSON object"),
) -> None:
    """Discard saved field values for selected tables."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.data_studio_table_discard_values(payload)))


@app.command("data-studio-table-edit")
def data_studio_table_edit(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Data Studio table edit JSON object"),
) -> None:
    """Bulk update selected tables."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.data_studio_table_edit(payload)))


@app.command("data-studio-table-rescan-values")
def data_studio_table_rescan_values(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Data Studio table selection JSON object"),
) -> None:
    """Rescan field values for selected tables."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.data_studio_table_rescan_values(payload)))


@app.command("data-studio-table-selection")
def data_studio_table_selection(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Data Studio table selection JSON object"),
) -> None:
    """Fetch information about selected tables."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.data_studio_table_selection(payload)))


@app.command("data-studio-table-sync-schema")
def data_studio_table_sync_schema(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Data Studio table selection JSON object"),
) -> None:
    """Sync schema for selected tables."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.data_studio_table_sync_schema(payload)))
