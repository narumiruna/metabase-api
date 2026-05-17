from __future__ import annotations

from typing import cast

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.preview_embed import GetPreviewEmbedCardParamRemappingRequest
from metabaseapi.endpoints.requests.preview_embed import GetPreviewEmbedCardParamValuesRequest
from metabaseapi.endpoints.requests.preview_embed import GetPreviewEmbedCardQueryRequest
from metabaseapi.endpoints.requests.preview_embed import GetPreviewEmbedCardRequest
from metabaseapi.endpoints.requests.preview_embed import GetPreviewEmbedDashboardDashcardCardRequest
from metabaseapi.endpoints.requests.preview_embed import GetPreviewEmbedDashboardParamRemappingRequest
from metabaseapi.endpoints.requests.preview_embed import GetPreviewEmbedDashboardParamSearchRequest
from metabaseapi.endpoints.requests.preview_embed import GetPreviewEmbedDashboardParamValuesRequest
from metabaseapi.endpoints.requests.preview_embed import GetPreviewEmbedDashboardRequest
from metabaseapi.endpoints.requests.preview_embed import GetPreviewEmbedPivotCardQueryRequest
from metabaseapi.endpoints.requests.preview_embed import GetPreviewEmbedPivotDashboardDashcardCardRequest
from metabaseapi.endpoints.requests.preview_embed import GetPreviewEmbedTilesCardRequest
from metabaseapi.endpoints.requests.preview_embed import GetPreviewEmbedTilesDashboardDashcardCardRequest
from metabaseapi.wire import QueryParamValue


def _parse_optional_query_params_or_empty(raw: str | None) -> dict[str, QueryParamValue]:
    payload = parse_optional_json_object(raw, "params") or {}
    return cast("dict[str, QueryParamValue]", payload)


@app.command("get-preview-embed-card")
def get_preview_embed_card(ctx: typer.Context, token: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, GetPreviewEmbedCardRequest(token=token))


@app.command("get-preview-embed-card-param-remapping")
def get_preview_embed_card_param_remapping(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetPreviewEmbedCardParamRemappingRequest(
            token=token,
            param_key=param_key,
            parameters=_parse_optional_query_params_or_empty(params),
        ),
    )


@app.command("get-preview-embed-card-param-values")
def get_preview_embed_card_param_values(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetPreviewEmbedCardParamValuesRequest(
            token=token,
            param_key=param_key,
            parameters=_parse_optional_query_params_or_empty(params),
        ),
    )


@app.command("get-preview-embed-card-query")
def get_preview_embed_card_query(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Query parameters JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetPreviewEmbedCardQueryRequest(token=token, parameters=_parse_optional_query_params_or_empty(params)),
    )


@app.command("get-preview-embed-dashboard")
def get_preview_embed_dashboard(ctx: typer.Context, token: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, GetPreviewEmbedDashboardRequest(token=token))


@app.command("get-preview-embed-dashboard-card")
def get_preview_embed_dashboard_card(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    card_id: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Query parameters JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetPreviewEmbedDashboardDashcardCardRequest(
            token=token,
            dashcard_id=dashcard_id,
            card_id=card_id,
            parameters=_parse_optional_query_params_or_empty(params),
        ),
    )


@app.command("get-preview-embed-dashboard-param-remapping")
def get_preview_embed_dashboard_param_remapping(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetPreviewEmbedDashboardParamRemappingRequest(
            token=token,
            param_key=param_key,
            parameters=_parse_optional_query_params_or_empty(params),
        ),
    )


@app.command("get-preview-embed-dashboard-param-search")
def get_preview_embed_dashboard_param_search(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    prefix: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetPreviewEmbedDashboardParamSearchRequest(
            token=token,
            param_key=param_key,
            prefix=prefix,
            parameters=_parse_optional_query_params_or_empty(params),
        ),
    )


@app.command("get-preview-embed-dashboard-param-values")
def get_preview_embed_dashboard_param_values(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetPreviewEmbedDashboardParamValuesRequest(
            token=token,
            param_key=param_key,
            parameters=_parse_optional_query_params_or_empty(params),
        ),
    )


@app.command("get-preview-embed-pivot-card-query")
def get_preview_embed_pivot_card_query(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Query parameters JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetPreviewEmbedPivotCardQueryRequest(token=token, parameters=_parse_optional_query_params_or_empty(params)),
    )


@app.command("get-preview-embed-pivot-dashboard-card")
def get_preview_embed_pivot_dashboard_card(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    card_id: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Query parameters JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetPreviewEmbedPivotDashboardDashcardCardRequest(
            token=token,
            dashcard_id=dashcard_id,
            card_id=card_id,
            parameters=_parse_optional_query_params_or_empty(params),
        ),
    )


@app.command("get-preview-embed-card-tile")
def get_preview_embed_card_tile(
    ctx: typer.Context,
    token: str = typer.Argument(...),
    zoom: int = typer.Argument(...),
    x: int = typer.Argument(...),
    y: int = typer.Argument(...),
) -> None:
    run_endpoint_command(ctx, GetPreviewEmbedTilesCardRequest(token=token, zoom=zoom, x=x, y=y))


@app.command("get-preview-embed-dashboard-card-tile")
def get_preview_embed_dashboard_card_tile(
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
        GetPreviewEmbedTilesDashboardDashcardCardRequest(
            token=token,
            dashcard_id=dashcard_id,
            card_id=card_id,
            zoom=zoom,
            x=x,
            y=y,
        ),
    )
