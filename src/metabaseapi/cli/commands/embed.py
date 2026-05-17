from __future__ import annotations

from typing import cast

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.embed import GetEmbedCardParamRemappingRequest
from metabaseapi.endpoints.requests.embed import GetEmbedCardParamSearchRequest
from metabaseapi.endpoints.requests.embed import GetEmbedCardParamValuesRequest
from metabaseapi.endpoints.requests.embed import GetEmbedCardQueryExportRequest
from metabaseapi.endpoints.requests.embed import GetEmbedCardQueryRequest
from metabaseapi.endpoints.requests.embed import GetEmbedCardRequest
from metabaseapi.endpoints.requests.embed import GetEmbedDashboardDashcardCardExportRequest
from metabaseapi.endpoints.requests.embed import GetEmbedDashboardDashcardCardRequest
from metabaseapi.endpoints.requests.embed import GetEmbedDashboardParamRemappingRequest
from metabaseapi.endpoints.requests.embed import GetEmbedDashboardParamSearchRequest
from metabaseapi.endpoints.requests.embed import GetEmbedDashboardParamValuesRequest
from metabaseapi.endpoints.requests.embed import GetEmbedDashboardRequest
from metabaseapi.endpoints.requests.embed import GetEmbedPivotCardQueryRequest
from metabaseapi.endpoints.requests.embed import GetEmbedPivotDashboardDashcardCardRequest
from metabaseapi.endpoints.requests.embed import GetEmbedTilesCardRequest
from metabaseapi.endpoints.requests.embed import GetEmbedTilesDashboardDashcardCardRequest
from metabaseapi.wire import QueryParamValue


def _parse_optional_query_params_or_empty(raw: str | None) -> dict[str, QueryParamValue]:
    payload = parse_optional_json_object(raw, "params") or {}
    return cast("dict[str, QueryParamValue]", payload)


@app.command("get-embed-card")
def get_embed_card(ctx: typer.Context, token: str = typer.Argument(...)) -> None:
    """Fetch an embedded card."""

    run_endpoint_command(ctx, GetEmbedCardRequest(token=token))


@app.command("get-embed-card-param-remapping")
def get_embed_card_param_remapping(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetEmbedCardParamRemappingRequest(
            token=token,
            param_key=param_key,
            parameters=_parse_optional_query_params_or_empty(params),
        ),
    )


@app.command("get-embed-card-param-search")
def get_embed_card_param_search(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    prefix: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetEmbedCardParamSearchRequest(
            token=token,
            param_key=param_key,
            prefix=prefix,
            parameters=_parse_optional_query_params_or_empty(params),
        ),
    )


@app.command("get-embed-card-param-values")
def get_embed_card_param_values(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetEmbedCardParamValuesRequest(
            token=token,
            param_key=param_key,
            parameters=_parse_optional_query_params_or_empty(params),
        ),
    )


@app.command("get-embed-card-query")
def get_embed_card_query(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Query parameters JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetEmbedCardQueryRequest(token=token, parameters=_parse_optional_query_params_or_empty(params)),
    )


@app.command("export-embed-card-query")
def export_embed_card_query(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    export_format: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Query parameters JSON object"),
    pivot_results: bool | None = typer.Option(None, "--pivot-results"),
    format_rows: bool | None = typer.Option(None, "--format-rows"),
) -> None:
    run_endpoint_command(
        ctx,
        GetEmbedCardQueryExportRequest(
            token=token,
            export_format=export_format,
            parameters=_parse_optional_query_params_or_empty(params),
            pivot_results=pivot_results,
            format_rows=format_rows,
        ),
    )


@app.command("get-embed-dashboard")
def get_embed_dashboard(ctx: typer.Context, token: str = typer.Argument(...)) -> None:
    """Fetch an embedded dashboard."""

    run_endpoint_command(ctx, GetEmbedDashboardRequest(token=token))


@app.command("get-embed-dashboard-card")
def get_embed_dashboard_card(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    card_id: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Query parameters JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetEmbedDashboardDashcardCardRequest(
            token=token,
            dashcard_id=dashcard_id,
            card_id=card_id,
            parameters=_parse_optional_query_params_or_empty(params),
        ),
    )


@app.command("export-embed-dashboard-card")
def export_embed_dashboard_card(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    card_id: str = typer.Argument(...),
    export_format: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Query parameters JSON object"),
    pivot_results: bool | None = typer.Option(None, "--pivot-results"),
    format_rows: bool | None = typer.Option(None, "--format-rows"),
) -> None:
    run_endpoint_command(
        ctx,
        GetEmbedDashboardDashcardCardExportRequest(
            token=token,
            dashcard_id=dashcard_id,
            card_id=card_id,
            export_format=export_format,
            parameters=_parse_optional_query_params_or_empty(params),
            pivot_results=pivot_results,
            format_rows=format_rows,
        ),
    )


@app.command("get-embed-dashboard-param-remapping")
def get_embed_dashboard_param_remapping(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetEmbedDashboardParamRemappingRequest(
            token=token,
            param_key=param_key,
            parameters=_parse_optional_query_params_or_empty(params),
        ),
    )


@app.command("get-embed-dashboard-param-search")
def get_embed_dashboard_param_search(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    prefix: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetEmbedDashboardParamSearchRequest(
            token=token,
            param_key=param_key,
            prefix=prefix,
            parameters=_parse_optional_query_params_or_empty(params),
        ),
    )


@app.command("get-embed-dashboard-param-values")
def get_embed_dashboard_param_values(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetEmbedDashboardParamValuesRequest(
            token=token,
            param_key=param_key,
            parameters=_parse_optional_query_params_or_empty(params),
        ),
    )


@app.command("get-embed-pivot-card-query")
def get_embed_pivot_card_query(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Query parameters JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetEmbedPivotCardQueryRequest(token=token, parameters=_parse_optional_query_params_or_empty(params)),
    )


@app.command("get-embed-pivot-dashboard-card")
def get_embed_pivot_dashboard_card(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    card_id: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Query parameters JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetEmbedPivotDashboardDashcardCardRequest(
            token=token,
            dashcard_id=dashcard_id,
            card_id=card_id,
            parameters=_parse_optional_query_params_or_empty(params),
        ),
    )


@app.command("get-embed-card-tile")
def get_embed_card_tile(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    zoom: int = typer.Argument(...),
    x: int = typer.Argument(...),
    y: int = typer.Argument(...),
) -> None:
    run_endpoint_command(ctx, GetEmbedTilesCardRequest(token=token, zoom=zoom, x=x, y=y))


@app.command("get-embed-dashboard-card-tile")
def get_embed_dashboard_card_tile(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    card_id: str = typer.Argument(...),
    zoom: int = typer.Argument(...),
    x: int = typer.Argument(...),
    y: int = typer.Argument(...),
) -> None:
    run_endpoint_command(
        ctx,
        GetEmbedTilesDashboardDashcardCardRequest(
            token=token,
            dashcard_id=dashcard_id,
            card_id=card_id,
            zoom=zoom,
            x=x,
            y=y,
        ),
    )
