from __future__ import annotations

from typing import cast

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_id_values
from metabaseapi.cli.runtime import parse_optional_json_object
from metabaseapi.cli.runtime import parse_optional_json_object_or_empty
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.dashboard_query import DashboardCardQueryExportRequest
from metabaseapi.endpoints.requests.dashboard_query import DashboardCardQueryRequest
from metabaseapi.endpoints.requests.dashboard_query import DashboardParamRemappingRequest
from metabaseapi.endpoints.requests.dashboard_query import DashboardParamSearchRequest
from metabaseapi.endpoints.requests.dashboard_query import DashboardParamsValidFilterFieldsRequest
from metabaseapi.endpoints.requests.dashboard_query import DashboardParamValuesRequest
from metabaseapi.endpoints.requests.dashboard_query import ExecuteDashboardDashcardRequest
from metabaseapi.endpoints.requests.dashboard_query import GetDashboardDashcardExecuteRequest
from metabaseapi.endpoints.requests.dashboard_query import GetDashboardQueryMetadataRequest
from metabaseapi.endpoints.requests.dashboard_query import GetDashboardRelatedRequest
from metabaseapi.endpoints.requests.dashboard_query import PostDashboardPivotQueryRequest
from metabaseapi.wire import QueryParamPrimitive
from metabaseapi.wire import QueryParamValue

_FILTERED_OPTION = typer.Option(None, "--filtered", help="Filtered field ID list")
_FILTERING_OPTION = typer.Option(None, "--filtering", help="Filtering field ID list")


def _parse_optional_query_params(raw: str | None) -> dict[str, QueryParamValue] | None:
    payload = parse_optional_json_object(raw, "params")
    return cast("dict[str, QueryParamValue] | None", payload)


def _parse_optional_query_params_or_empty(raw: str | None) -> dict[str, QueryParamValue]:
    return _parse_optional_query_params(raw) or {}


@app.command("get-dashboard-params-valid-filter-fields")
def get_dashboard_params_valid_filter_fields(
    ctx: typer.Context,
    filtered: list[str] | None = _FILTERED_OPTION,
    filtering: list[str] | None = _FILTERING_OPTION,
) -> None:
    """Get valid filter fields for dashboard parameters."""

    run_endpoint_command(
        ctx,
        DashboardParamsValidFilterFieldsRequest(
            filtered=cast("list[QueryParamPrimitive] | None", parse_id_values(filtered or []) or None),
            filtering=cast("list[QueryParamPrimitive] | None", parse_id_values(filtering or []) or None),
        ),
    )


@app.command("query-dashboard-card")
def query_dashboard_card(
    ctx: typer.Context,
    dashboard_id: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    card_id: str = typer.Argument(...),
    body: str = typer.Argument(None, help="Optional query payload JSON object"),
) -> None:
    payload = parse_optional_json_object(body, "body")
    run_endpoint_command(
        ctx,
        DashboardCardQueryRequest(
            dashboard_id=dashboard_id,
            dashcard_id=dashcard_id,
            card_id=card_id,
            body=payload,
        ),
    )


@app.command("query-dashboard-card-export")
def query_dashboard_card_export(
    ctx: typer.Context,
    dashboard_id: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    card_id: str = typer.Argument(...),
    export_format: str = typer.Argument(...),
    body: str = typer.Argument(None, help="Optional query payload JSON object"),
    pivot_results: bool | None = typer.Option(None, "--pivot-results"),
    format_rows: bool | None = typer.Option(None, "--format-rows"),
) -> None:
    payload = parse_optional_json_object(body, "body")
    run_endpoint_command(
        ctx,
        DashboardCardQueryExportRequest(
            dashboard_id=dashboard_id,
            dashcard_id=dashcard_id,
            card_id=card_id,
            export_format=export_format,
            body=payload,
            pivot_results=pivot_results,
            format_rows=format_rows,
        ),
    )


@app.command("query-dashboard-card-pivot")
def query_dashboard_card_pivot(
    ctx: typer.Context,
    dashboard_id: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    card_id: str = typer.Argument(...),
    body: str | None = typer.Argument(None, help="Optional query payload JSON object"),
) -> None:
    payload = parse_optional_json_object(body, "body")
    run_endpoint_command(
        ctx,
        PostDashboardPivotQueryRequest(
            dashboard_id=dashboard_id,
            dashcard_id=dashcard_id,
            card_id=card_id,
            body=payload,
        ),
    )


@app.command("get-dashboard-dashcard-execute")
def get_dashboard_dashcard_execute(
    ctx: typer.Context,
    dashboard_id: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Execution query parameters JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetDashboardDashcardExecuteRequest(
            dashboard_id=dashboard_id,
            dashcard_id=dashcard_id,
            parameters=_parse_optional_query_params_or_empty(params),
        ),
    )


@app.command("execute-dashboard-dashcard")
def execute_dashboard_dashcard(
    ctx: typer.Context,
    dashboard_id: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    parameters: str | None = typer.Option(None, "--parameters", help="Execution parameters JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        ExecuteDashboardDashcardRequest(
            dashboard_id=dashboard_id,
            dashcard_id=dashcard_id,
            parameters=parse_optional_json_object_or_empty(parameters, "parameters"),
        ),
    )


@app.command("get-dashboard-param-remapping")
def get_dashboard_param_remapping(
    ctx: typer.Context,
    dashboard_id: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        DashboardParamRemappingRequest(
            dashboard_id=dashboard_id,
            param_key=param_key,
            parameters=_parse_optional_query_params_or_empty(params),
        ),
    )


@app.command("get-dashboard-param-search")
def get_dashboard_param_search_values(
    ctx: typer.Context,
    dashboard_id: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    query: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        DashboardParamSearchRequest(
            dashboard_id=dashboard_id,
            param_key=param_key,
            query=query,
            parameters=_parse_optional_query_params_or_empty(params),
        ),
    )


@app.command("get-dashboard-param-values")
def get_dashboard_param_values(
    ctx: typer.Context,
    dashboard_id: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        DashboardParamValuesRequest(
            dashboard_id=dashboard_id,
            param_key=param_key,
            parameters=_parse_optional_query_params_or_empty(params),
        ),
    )


@app.command("get-dashboard-query-metadata")
def get_dashboard_query_metadata(ctx: typer.Context, dashboard_id: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, GetDashboardQueryMetadataRequest(dashboard_id=dashboard_id))


@app.command("get-dashboard-related")
def get_dashboard_related(ctx: typer.Context, dashboard_id: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, GetDashboardRelatedRequest(dashboard_id=dashboard_id))
