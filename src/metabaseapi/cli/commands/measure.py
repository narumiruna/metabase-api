from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.measure import CreateMeasureRequest
from metabaseapi.endpoints.requests.measure import GetMeasureDimensionRemappingRequest
from metabaseapi.endpoints.requests.measure import GetMeasureDimensionValuesRequest
from metabaseapi.endpoints.requests.measure import GetMeasureRequest
from metabaseapi.endpoints.requests.measure import ListMeasuresRequest
from metabaseapi.endpoints.requests.measure import SearchMeasureDimensionValuesRequest
from metabaseapi.endpoints.requests.measure import UpdateMeasureRequest
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


@app.command("create-measure")
def create_measure(ctx: typer.Context, body: str = typer.Argument(..., help="Measure JSON object")) -> None:
    """Create a measure."""

    run_json_body_endpoint_command(ctx, body, lambda payload: CreateMeasureRequest(body=payload))


@app.command("list-measures")
def list_measures(ctx: typer.Context) -> None:
    """List measures."""

    run_endpoint_command(ctx, ListMeasuresRequest())


@app.command("get-measure")
def get_measure(ctx: typer.Context, measure_id: str = typer.Argument(...)) -> None:
    """Get a measure by ID."""

    run_endpoint_command(ctx, GetMeasureRequest(measure_id=measure_id))


@app.command("update-measure")
def update_measure(
    ctx: typer.Context,
    measure_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Measure update JSON object"),
) -> None:
    """Update a measure."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateMeasureRequest(measure_id=measure_id, body=payload))


@app.command("get-measure-dimension-remapping")
def get_measure_dimension_remapping(
    ctx: typer.Context,
    measure_id: str = typer.Argument(...),
    dimension_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Dimension remapping query params JSON object"),
) -> None:
    """Get measure dimension remapping values."""

    run_endpoint_command(
        ctx,
        GetMeasureDimensionRemappingRequest(
            measure_id=measure_id,
            dimension_key=dimension_key,
            params=_parse_query_params(params),
        ),
    )


@app.command("search-measure-dimension-values")
def search_measure_dimension_values(
    ctx: typer.Context,
    measure_id: str = typer.Argument(...),
    dimension_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Dimension search query params JSON object"),
) -> None:
    """Search measure dimension values."""

    run_endpoint_command(
        ctx,
        SearchMeasureDimensionValuesRequest(
            measure_id=measure_id,
            dimension_key=dimension_key,
            params=_parse_query_params(params),
        ),
    )


@app.command("get-measure-dimension-values")
def get_measure_dimension_values(
    ctx: typer.Context,
    measure_id: str = typer.Argument(...),
    dimension_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Dimension values query params JSON object"),
) -> None:
    """Get measure dimension values."""

    run_endpoint_command(
        ctx,
        GetMeasureDimensionValuesRequest(
            measure_id=measure_id,
            dimension_key=dimension_key,
            params=_parse_query_params(params),
        ),
    )
