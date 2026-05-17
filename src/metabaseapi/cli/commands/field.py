from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.field import DeleteFieldDimensionRequest
from metabaseapi.endpoints.requests.field import DiscardFieldValuesRequest
from metabaseapi.endpoints.requests.field import GetFieldRelatedRequest
from metabaseapi.endpoints.requests.field import GetFieldRemappingRequest
from metabaseapi.endpoints.requests.field import GetFieldRequest
from metabaseapi.endpoints.requests.field import GetFieldSummaryRequest
from metabaseapi.endpoints.requests.field import GetFieldValuesRequest
from metabaseapi.endpoints.requests.field import RescanFieldValuesRequest
from metabaseapi.endpoints.requests.field import SearchFieldValuesRequest
from metabaseapi.endpoints.requests.field import SetFieldDimensionRequest
from metabaseapi.endpoints.requests.field import UpdateFieldRequest
from metabaseapi.endpoints.requests.field import UpdateFieldValuesRequest
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


@app.command("get-field")
def get_field(ctx: typer.Context, field_id: str = typer.Argument(...)) -> None:
    """Get a field by ID."""

    run_endpoint_command(ctx, GetFieldRequest(field_id=field_id))


@app.command("update-field")
def update_field(
    ctx: typer.Context,
    field_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Field update JSON object"),
) -> None:
    """Update a field."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateFieldRequest(field_id=field_id, body=payload))


@app.command("set-field-dimension")
def set_field_dimension(
    ctx: typer.Context,
    field_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Field dimension JSON object"),
) -> None:
    """Set the dimension for a field."""

    run_json_body_endpoint_command(ctx, body, lambda payload: SetFieldDimensionRequest(field_id=field_id, body=payload))


@app.command("delete-field-dimension")
def delete_field_dimension(ctx: typer.Context, field_id: str = typer.Argument(...)) -> None:
    """Remove the dimension for a field."""

    run_endpoint_command(ctx, DeleteFieldDimensionRequest(field_id=field_id))


@app.command("discard-field-values")
def discard_field_values(ctx: typer.Context, field_id: str = typer.Argument(...)) -> None:
    """Discard saved values for a field."""

    run_endpoint_command(ctx, DiscardFieldValuesRequest(field_id=field_id))


@app.command("get-field-related")
def get_field_related(ctx: typer.Context, field_id: str = typer.Argument(...)) -> None:
    """Get entities related to a field."""

    run_endpoint_command(ctx, GetFieldRelatedRequest(field_id=field_id))


@app.command("get-field-remapping")
def get_field_remapping(
    ctx: typer.Context,
    field_id: str = typer.Argument(...),
    remapped_id: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Remapping query params JSON object"),
) -> None:
    """Get remapped field values."""

    run_endpoint_command(
        ctx,
        GetFieldRemappingRequest(field_id=field_id, remapped_id=remapped_id, params=_parse_query_params(params)),
    )


@app.command("rescan-field-values")
def rescan_field_values(ctx: typer.Context, field_id: str = typer.Argument(...)) -> None:
    """Rescan saved values for a field."""

    run_endpoint_command(ctx, RescanFieldValuesRequest(field_id=field_id))


@app.command("search-field-values")
def search_field_values(
    ctx: typer.Context,
    field_id: str = typer.Argument(...),
    search_id: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Search query params JSON object"),
) -> None:
    """Search field values."""

    run_endpoint_command(
        ctx,
        SearchFieldValuesRequest(field_id=field_id, search_id=search_id, params=_parse_query_params(params)),
    )


@app.command("get-field-summary")
def get_field_summary(ctx: typer.Context, field_id: str = typer.Argument(...)) -> None:
    """Get field counts."""

    run_endpoint_command(ctx, GetFieldSummaryRequest(field_id=field_id))


@app.command("get-field-values")
def get_field_values(ctx: typer.Context, field_id: str = typer.Argument(...)) -> None:
    """Get field values."""

    run_endpoint_command(ctx, GetFieldValuesRequest(field_id=field_id))


@app.command("update-field-values")
def update_field_values(
    ctx: typer.Context,
    field_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Field values JSON object"),
) -> None:
    """Update field values."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateFieldValuesRequest(field_id=field_id, body=payload))
