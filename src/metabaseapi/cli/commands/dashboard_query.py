from __future__ import annotations

from typing import cast

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object
from metabaseapi.cli.runtime import run_client_command
from metabaseapi.client.raw import dashboard as _raw_dashboard
from metabaseapi.client.raw import dashboard_query as _raw_dashboard_query
from metabaseapi.wire import QueryParamValue

_FILTERED_OPTION = typer.Option(None, "--filtered", help="Filtered field ID list")
_FILTERING_OPTION = typer.Option(None, "--filtering", help="Filtering field ID list")


def _parse_optional_query_params(raw: str | None) -> dict[str, QueryParamValue] | None:
    payload = parse_optional_json_object(raw, "params")
    return cast("dict[str, QueryParamValue] | None", payload)


@app.command("get-dashboard")
def get_dashboard(ctx: typer.Context, dashboard_id: str = typer.Argument(...)) -> None:
    """Get a dashboard by ID."""

    run_client_command(ctx, lambda client: _raw_dashboard.get_dashboard(client, dashboard_id))


@app.command("get-dashboard-params-valid-filter-fields")
def get_dashboard_params_valid_filter_fields(
    ctx: typer.Context,
    filtered: list[str] | None = _FILTERED_OPTION,
    filtering: list[str] | None = _FILTERING_OPTION,
) -> None:
    """Get valid filter fields for dashboard parameters."""

    filtered_values = [int(item) if item.isdigit() else item for item in (filtered or [])]
    filtering_values = [int(item) if item.isdigit() else item for item in (filtering or [])]
    run_client_command(
        ctx,
        lambda client: _raw_dashboard_query.get_dashboard_params_valid_filter_fields(
            client,
            filtered=filtered_values or None,
            filtering=filtering_values or None,
        ),
    )


@app.command("get-dashboard-embeddable")
def get_dashboard_embeddable(ctx: typer.Context) -> None:
    """List embeddable dashboards."""

    run_client_command(
        ctx,
        lambda client: _raw_dashboard.get_dashboard_embeddable(
            client,
        ),
    )


@app.command("get-dashboard-public")
def get_dashboard_public(ctx: typer.Context) -> None:
    """List public dashboards."""

    run_client_command(
        ctx,
        lambda client: _raw_dashboard.get_dashboard_public(
            client,
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
    payload = parse_optional_json_object(body, "body") if body else None
    run_client_command(
        ctx,
        lambda client: _raw_dashboard_query.query_dashboard_card(
            client,
            dashboard_id,
            dashcard_id,
            card_id,
            payload,
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
    payload = parse_optional_json_object(body, "body") if body else None
    run_client_command(
        ctx,
        lambda client: _raw_dashboard_query.query_dashboard_card_export(
            client,
            dashboard_id,
            dashcard_id,
            card_id,
            export_format,
            payload,
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
    payload = parse_optional_json_object(body, "body") if body else None
    run_client_command(
        ctx,
        lambda client: _raw_dashboard_query.query_dashboard_card_pivot(
            client,
            dashboard_id,
            dashcard_id,
            card_id,
            payload,
        ),
    )


@app.command("get-dashboard-dashcard-execute")
def get_dashboard_dashcard_execute(
    ctx: typer.Context,
    dashboard_id: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Execution query parameters JSON object"),
) -> None:
    payload = _parse_optional_query_params(params)
    run_client_command(
        ctx,
        lambda client: _raw_dashboard_query.get_dashboard_dashcard_execute(
            client,
            dashboard_id,
            dashcard_id,
            parameters=payload,
        ),
    )


@app.command("execute-dashboard-dashcard")
def execute_dashboard_dashcard(
    ctx: typer.Context,
    dashboard_id: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    parameters: str | None = typer.Option(None, "--parameters", help="Execution parameters JSON object"),
) -> None:
    payload = parse_optional_json_object(parameters, "parameters")
    run_client_command(
        ctx,
        lambda client: _raw_dashboard_query.execute_dashboard_dashcard(
            client,
            dashboard_id,
            dashcard_id,
            parameters=payload,
        ),
    )


@app.command("get-dashboard-param-remapping")
def get_dashboard_param_remapping(
    ctx: typer.Context,
    dashboard_id: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    payload = _parse_optional_query_params(params)
    run_client_command(
        ctx,
        lambda client: _raw_dashboard_query.get_dashboard_param_remapping(
            client, dashboard_id, param_key, parameters=payload
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
    payload = _parse_optional_query_params(params)
    run_client_command(
        ctx,
        lambda client: _raw_dashboard_query.get_dashboard_param_search_values(
            client,
            dashboard_id,
            param_key,
            query,
            parameters=payload,
        ),
    )


@app.command("get-dashboard-param-values")
def get_dashboard_param_values(
    ctx: typer.Context,
    dashboard_id: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    payload = _parse_optional_query_params(params)
    run_client_command(
        ctx,
        lambda client: _raw_dashboard_query.get_dashboard_param_values(
            client, dashboard_id, param_key, parameters=payload
        ),
    )


@app.command("get-dashboard-query-metadata")
def get_dashboard_query_metadata(ctx: typer.Context, dashboard_id: str = typer.Argument(...)) -> None:
    run_client_command(ctx, lambda client: _raw_dashboard_query.get_dashboard_query_metadata(client, dashboard_id))


@app.command("get-dashboard-related")
def get_dashboard_related(ctx: typer.Context, dashboard_id: str = typer.Argument(...)) -> None:
    run_client_command(ctx, lambda client: _raw_dashboard_query.get_dashboard_related(client, dashboard_id))
