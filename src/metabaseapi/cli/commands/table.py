from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.table import AppendTableCsvRequest
from metabaseapi.endpoints.requests.table import DiscardTableValuesRequest
from metabaseapi.endpoints.requests.table import GetCardTableForeignKeysRequest
from metabaseapi.endpoints.requests.table import GetCardTableQueryMetadataRequest
from metabaseapi.endpoints.requests.table import GetTableDataRequest
from metabaseapi.endpoints.requests.table import GetTableForeignKeysRequest
from metabaseapi.endpoints.requests.table import GetTableQueryMetadataRequest
from metabaseapi.endpoints.requests.table import GetTableRelatedRequest
from metabaseapi.endpoints.requests.table import GetTableRequest
from metabaseapi.endpoints.requests.table import ListTablesRequest
from metabaseapi.endpoints.requests.table import ReplaceTableCsvRequest
from metabaseapi.endpoints.requests.table import RescanTableValuesRequest
from metabaseapi.endpoints.requests.table import SyncTableSchemaRequest
from metabaseapi.endpoints.requests.table import UpdateTableFieldsOrderRequest
from metabaseapi.endpoints.requests.table import UpdateTableRequest
from metabaseapi.endpoints.requests.table import UpdateTablesRequest
from metabaseapi.wire import QueryParamPrimitive
from metabaseapi.wire import QueryParamValue


def _parse_query_param_value(value: object) -> QueryParamValue | None:
    if isinstance(value, str | int | float | bool) or value is None:
        return value
    if isinstance(value, list):
        parsed_values: list[QueryParamPrimitive] = [
            item for item in value if isinstance(item, str | int | float | bool) or item is None
        ]
        return parsed_values
    return None


def _parse_query_params(raw: str | None) -> dict[str, QueryParamValue]:
    payload = parse_optional_json_object(raw, "params") or {}
    params: dict[str, QueryParamValue] = {}
    for key, value in payload.items():
        parsed_value = _parse_query_param_value(value)
        if parsed_value is not None:
            params[key] = parsed_value
    return params


@app.command("list-tables")
def list_tables(
    ctx: typer.Context,
    params: str | None = typer.Option(None, "--params", help="Table list query params JSON object"),
) -> None:
    """List tables."""

    run_endpoint_command(ctx, ListTablesRequest(params=_parse_query_params(params)))


@app.command("update-tables")
def update_tables(ctx: typer.Context, body: str = typer.Argument(..., help="Bulk table update JSON object")) -> None:
    """Update multiple tables."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateTablesRequest(body=payload))


@app.command("get-card-table-fks")
def get_card_table_fks(ctx: typer.Context, card_id: str = typer.Argument(...)) -> None:
    """Get foreign keys for a card virtual table."""

    run_endpoint_command(ctx, GetCardTableForeignKeysRequest(card_id=card_id))


@app.command("get-card-table-query-metadata")
def get_card_table_query_metadata(
    ctx: typer.Context,
    card_id: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Query metadata params JSON object"),
) -> None:
    """Get query metadata for a card virtual table."""

    run_endpoint_command(
        ctx,
        GetCardTableQueryMetadataRequest(card_id=card_id, params=_parse_query_params(params)),
    )


@app.command("get-table")
def get_table(ctx: typer.Context, table_id: str = typer.Argument(...)) -> None:
    """Get a table by ID."""

    run_endpoint_command(ctx, GetTableRequest(table_id=table_id))


@app.command("update-table")
def update_table(
    ctx: typer.Context,
    table_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Table update JSON object"),
) -> None:
    """Update a table."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateTableRequest(table_id=table_id, body=payload))


@app.command("append-table-csv")
def append_table_csv(
    ctx: typer.Context,
    table_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="CSV append JSON object"),
) -> None:
    """Append CSV rows to an uploaded table."""

    run_json_body_endpoint_command(ctx, body, lambda payload: AppendTableCsvRequest(table_id=table_id, body=payload))


@app.command("discard-table-values")
def discard_table_values(ctx: typer.Context, table_id: str = typer.Argument(...)) -> None:
    """Discard saved field values for a table."""

    run_endpoint_command(ctx, DiscardTableValuesRequest(table_id=table_id))


@app.command("update-table-fields-order")
def update_table_fields_order(
    ctx: typer.Context,
    table_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Field ordering JSON object"),
) -> None:
    """Reorder table fields."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: UpdateTableFieldsOrderRequest(table_id=table_id, body=payload),
    )


@app.command("get-table-fks")
def get_table_fks(ctx: typer.Context, table_id: str = typer.Argument(...)) -> None:
    """Get foreign keys for a table."""

    run_endpoint_command(ctx, GetTableForeignKeysRequest(table_id=table_id))


@app.command("get-table-query-metadata")
def get_table_query_metadata(
    ctx: typer.Context,
    table_id: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Query metadata params JSON object"),
) -> None:
    """Get query metadata for a table."""

    run_endpoint_command(ctx, GetTableQueryMetadataRequest(table_id=table_id, params=_parse_query_params(params)))


@app.command("get-table-related")
def get_table_related(ctx: typer.Context, table_id: str = typer.Argument(...)) -> None:
    """Get related entities for a table."""

    run_endpoint_command(ctx, GetTableRelatedRequest(table_id=table_id))


@app.command("replace-table-csv")
def replace_table_csv(
    ctx: typer.Context,
    table_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="CSV replacement JSON object"),
) -> None:
    """Replace uploaded table rows with CSV rows."""

    run_json_body_endpoint_command(ctx, body, lambda payload: ReplaceTableCsvRequest(table_id=table_id, body=payload))


@app.command("rescan-table-values")
def rescan_table_values(ctx: typer.Context, table_id: str = typer.Argument(...)) -> None:
    """Rescan saved field values for a table."""

    run_endpoint_command(ctx, RescanTableValuesRequest(table_id=table_id))


@app.command("sync-table-schema")
def sync_table_schema(ctx: typer.Context, table_id: str = typer.Argument(...)) -> None:
    """Trigger a schema sync for a table."""

    run_endpoint_command(ctx, SyncTableSchemaRequest(table_id=table_id))


@app.command("get-table-data")
def get_table_data(
    ctx: typer.Context,
    table_id: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Table data params JSON object"),
) -> None:
    """Get data for a table."""

    run_endpoint_command(ctx, GetTableDataRequest(table_id=table_id, params=_parse_query_params(params)))
