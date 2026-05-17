from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.data_studio import DataStudioTableDiscardValuesRequest
from metabaseapi.endpoints.requests.data_studio import DataStudioTableEditRequest
from metabaseapi.endpoints.requests.data_studio import DataStudioTableRescanValuesRequest
from metabaseapi.endpoints.requests.data_studio import DataStudioTableSelectionRequest
from metabaseapi.endpoints.requests.data_studio import DataStudioTableSyncSchemaRequest


@app.command("data-studio-table-discard-values")
def data_studio_table_discard_values(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Data Studio table selection JSON object"),
) -> None:
    """Discard saved field values for selected tables."""

    run_json_body_endpoint_command(ctx, body, lambda payload: DataStudioTableDiscardValuesRequest(body=payload))


@app.command("data-studio-table-edit")
def data_studio_table_edit(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Data Studio table edit JSON object"),
) -> None:
    """Bulk update selected tables."""

    run_json_body_endpoint_command(ctx, body, lambda payload: DataStudioTableEditRequest(body=payload))


@app.command("data-studio-table-rescan-values")
def data_studio_table_rescan_values(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Data Studio table selection JSON object"),
) -> None:
    """Rescan field values for selected tables."""

    run_json_body_endpoint_command(ctx, body, lambda payload: DataStudioTableRescanValuesRequest(body=payload))


@app.command("data-studio-table-selection")
def data_studio_table_selection(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Data Studio table selection JSON object"),
) -> None:
    """Fetch information about selected tables."""

    run_json_body_endpoint_command(ctx, body, lambda payload: DataStudioTableSelectionRequest(body=payload))


@app.command("data-studio-table-sync-schema")
def data_studio_table_sync_schema(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Data Studio table selection JSON object"),
) -> None:
    """Sync schema for selected tables."""

    run_json_body_endpoint_command(ctx, body, lambda payload: DataStudioTableSyncSchemaRequest(body=payload))
