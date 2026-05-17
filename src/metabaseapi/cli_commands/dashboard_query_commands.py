from __future__ import annotations

from typing import cast

import typer

from metabaseapi.cli import _parse_optional_json_object
from metabaseapi.cli import _run_and_print
from metabaseapi.cli import _run_client_call
from metabaseapi.cli import app
from metabaseapi.models import QueryParamValue

_FILTERED_OPTION = typer.Option(None, "--filtered", help="Filtered field ID list")
_FILTERING_OPTION = typer.Option(None, "--filtering", help="Filtering field ID list")


def _parse_optional_query_params(raw: str | None) -> dict[str, QueryParamValue] | None:
    payload = _parse_optional_json_object(raw, "params")
    return cast("dict[str, QueryParamValue] | None", payload)


@app.command("get-dashboard")
def get_dashboard(ctx: typer.Context, dashboard_id: str = typer.Argument(...)) -> None:
    """Get a dashboard by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_dashboard(dashboard_id)))


@app.command("get-dashboard-params-valid-filter-fields")
def get_dashboard_params_valid_filter_fields(
    ctx: typer.Context,
    filtered: list[str] | None = _FILTERED_OPTION,
    filtering: list[str] | None = _FILTERING_OPTION,
) -> None:
    """Get valid filter fields for dashboard parameters."""

    filtered_values = [int(item) if item.isdigit() else item for item in (filtered or [])]
    filtering_values = [int(item) if item.isdigit() else item for item in (filtering or [])]
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.get_dashboard_params_valid_filter_fields(
                filtered=filtered_values or None,
                filtering=filtering_values or None,
            ),
        )
    )


@app.command("get-dashboard-embeddable")
def get_dashboard_embeddable(ctx: typer.Context) -> None:
    """List embeddable dashboards."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_dashboard_embeddable()))


@app.command("get-dashboard-public")
def get_dashboard_public(ctx: typer.Context) -> None:
    """List public dashboards."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_dashboard_public()))


@app.command("query-dashboard-card")
def query_dashboard_card(
    ctx: typer.Context,
    dashboard_id: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    card_id: str = typer.Argument(...),
    body: str = typer.Argument(None, help="Optional query payload JSON object"),
) -> None:
    payload = _parse_optional_json_object(body, "body") if body else None
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.query_dashboard_card(
                dashboard_id,
                dashcard_id,
                card_id,
                payload,
            ),
        )
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
    payload = _parse_optional_json_object(body, "body") if body else None
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.query_dashboard_card_export(
                dashboard_id,
                dashcard_id,
                card_id,
                export_format,
                payload,
                pivot_results=pivot_results,
                format_rows=format_rows,
            ),
        )
    )


@app.command("query-dashboard-card-pivot")
def query_dashboard_card_pivot(
    ctx: typer.Context,
    dashboard_id: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    card_id: str = typer.Argument(...),
    body: str | None = typer.Argument(None, help="Optional query payload JSON object"),
) -> None:
    payload = _parse_optional_json_object(body, "body") if body else None
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.query_dashboard_card_pivot(
                dashboard_id,
                dashcard_id,
                card_id,
                payload,
            ),
        )
    )


@app.command("get-dashboard-dashcard-execute")
def get_dashboard_dashcard_execute(
    ctx: typer.Context,
    dashboard_id: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Execution query parameters JSON object"),
) -> None:
    payload = _parse_optional_query_params(params)
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.get_dashboard_dashcard_execute(
                dashboard_id,
                dashcard_id,
                parameters=payload,
            ),
        )
    )


@app.command("execute-dashboard-dashcard")
def execute_dashboard_dashcard(
    ctx: typer.Context,
    dashboard_id: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    parameters: str | None = typer.Option(None, "--parameters", help="Execution parameters JSON object"),
) -> None:
    payload = _parse_optional_json_object(parameters, "parameters")
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.execute_dashboard_dashcard(
                dashboard_id,
                dashcard_id,
                parameters=payload,
            ),
        )
    )


@app.command("get-dashboard-param-remapping")
def get_dashboard_param_remapping(
    ctx: typer.Context,
    dashboard_id: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    payload = _parse_optional_query_params(params)
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.get_dashboard_param_remapping(dashboard_id, param_key, parameters=payload),
        )
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
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.get_dashboard_param_search_values(
                dashboard_id,
                param_key,
                query,
                parameters=payload,
            ),
        )
    )


@app.command("get-dashboard-param-values")
def get_dashboard_param_values(
    ctx: typer.Context,
    dashboard_id: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    payload = _parse_optional_query_params(params)
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.get_dashboard_param_values(dashboard_id, param_key, parameters=payload),
        )
    )


@app.command("get-dashboard-query-metadata")
def get_dashboard_query_metadata(ctx: typer.Context, dashboard_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_dashboard_query_metadata(dashboard_id)))


@app.command("get-dashboard-related")
def get_dashboard_related(ctx: typer.Context, dashboard_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_dashboard_related(dashboard_id)))
