from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_json_object
from metabaseapi.cli.runtime import run_endpoint_command
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

    payload = parse_json_object(body, "body")
    run_endpoint_command(ctx, DataStudioTableDiscardValuesRequest(body=payload))


@app.command("data-studio-table-edit")
def data_studio_table_edit(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Data Studio table edit JSON object"),
) -> None:
    """Bulk update selected tables."""

    payload = parse_json_object(body, "body")
    run_endpoint_command(ctx, DataStudioTableEditRequest(body=payload))


@app.command("data-studio-table-rescan-values")
def data_studio_table_rescan_values(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Data Studio table selection JSON object"),
) -> None:
    """Rescan field values for selected tables."""

    payload = parse_json_object(body, "body")
    run_endpoint_command(ctx, DataStudioTableRescanValuesRequest(body=payload))


@app.command("data-studio-table-selection")
def data_studio_table_selection(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Data Studio table selection JSON object"),
) -> None:
    """Fetch information about selected tables."""

    payload = parse_json_object(body, "body")
    run_endpoint_command(ctx, DataStudioTableSelectionRequest(body=payload))


@app.command("data-studio-table-sync-schema")
def data_studio_table_sync_schema(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Data Studio table selection JSON object"),
) -> None:
    """Sync schema for selected tables."""

    payload = parse_json_object(body, "body")
    run_endpoint_command(ctx, DataStudioTableSyncSchemaRequest(body=payload))
