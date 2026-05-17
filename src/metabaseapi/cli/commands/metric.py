from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.metric import GetMetricDimensionRemappingRequest
from metabaseapi.endpoints.requests.metric import GetMetricDimensionValuesRequest
from metabaseapi.endpoints.requests.metric import GetMetricRequest
from metabaseapi.endpoints.requests.metric import ListMetricsRequest
from metabaseapi.endpoints.requests.metric import MetricBreakoutValuesRequest
from metabaseapi.endpoints.requests.metric import MetricDatasetRequest
from metabaseapi.endpoints.requests.metric import SearchMetricDimensionValuesRequest
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


@app.command("list-metrics")
def list_metrics(ctx: typer.Context) -> None:
    """List metrics."""

    run_endpoint_command(ctx, ListMetricsRequest())


@app.command("post-metric-breakout-values")
def post_metric_breakout_values(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Metric breakout values JSON object"),
) -> None:
    """Fetch distinct breakout dimension values for a metric definition."""

    run_json_body_endpoint_command(ctx, body, lambda payload: MetricBreakoutValuesRequest(body=payload))


@app.command("post-metric-dataset")
def post_metric_dataset(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Metric dataset JSON object"),
) -> None:
    """Execute a metric or measure-based query."""

    run_json_body_endpoint_command(ctx, body, lambda payload: MetricDatasetRequest(body=payload))


@app.command("get-metric")
def get_metric(ctx: typer.Context, metric_id: str = typer.Argument(...)) -> None:
    """Get a metric by ID."""

    run_endpoint_command(ctx, GetMetricRequest(metric_id=metric_id))


@app.command("get-metric-dimension-remapping")
def get_metric_dimension_remapping(
    ctx: typer.Context,
    metric_id: str = typer.Argument(...),
    dimension_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Dimension remapping query params JSON object"),
) -> None:
    """Get metric dimension remapping values."""

    run_endpoint_command(
        ctx,
        GetMetricDimensionRemappingRequest(
            metric_id=metric_id,
            dimension_key=dimension_key,
            params=_parse_query_params(params),
        ),
    )


@app.command("search-metric-dimension-values")
def search_metric_dimension_values(
    ctx: typer.Context,
    metric_id: str = typer.Argument(...),
    dimension_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Dimension search query params JSON object"),
) -> None:
    """Search metric dimension values."""

    run_endpoint_command(
        ctx,
        SearchMetricDimensionValuesRequest(
            metric_id=metric_id,
            dimension_key=dimension_key,
            params=_parse_query_params(params),
        ),
    )


@app.command("get-metric-dimension-values")
def get_metric_dimension_values(
    ctx: typer.Context,
    metric_id: str = typer.Argument(...),
    dimension_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Dimension values query params JSON object"),
) -> None:
    """Get metric dimension values."""

    run_endpoint_command(
        ctx,
        GetMetricDimensionValuesRequest(
            metric_id=metric_id,
            dimension_key=dimension_key,
            params=_parse_query_params(params),
        ),
    )
