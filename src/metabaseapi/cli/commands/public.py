from __future__ import annotations

from typing import cast

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object
from metabaseapi.cli.runtime import parse_optional_json_object_or_empty
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.public import ExecutePublicActionRequest
from metabaseapi.endpoints.requests.public import ExecutePublicDashboardDashcardRequest
from metabaseapi.endpoints.requests.public import ExportPublicDashboardCardRequest
from metabaseapi.endpoints.requests.public import ExportPublicDocumentCardRequest
from metabaseapi.endpoints.requests.public import GetPublicActionRequest
from metabaseapi.endpoints.requests.public import GetPublicCardParamRemappingRequest
from metabaseapi.endpoints.requests.public import GetPublicCardParamSearchRequest
from metabaseapi.endpoints.requests.public import GetPublicCardParamValuesRequest
from metabaseapi.endpoints.requests.public import GetPublicCardQueryExportRequest
from metabaseapi.endpoints.requests.public import GetPublicCardQueryRequest
from metabaseapi.endpoints.requests.public import GetPublicCardRequest
from metabaseapi.endpoints.requests.public import GetPublicCardTileRequest
from metabaseapi.endpoints.requests.public import GetPublicDashboardCardRequest
from metabaseapi.endpoints.requests.public import GetPublicDashboardCardTileRequest
from metabaseapi.endpoints.requests.public import GetPublicDashboardDashcardExecuteRequest
from metabaseapi.endpoints.requests.public import GetPublicDashboardParamRemappingRequest
from metabaseapi.endpoints.requests.public import GetPublicDashboardParamSearchRequest
from metabaseapi.endpoints.requests.public import GetPublicDashboardParamValuesRequest
from metabaseapi.endpoints.requests.public import GetPublicDashboardRequest
from metabaseapi.endpoints.requests.public import GetPublicDocumentCardRequest
from metabaseapi.endpoints.requests.public import GetPublicDocumentRequest
from metabaseapi.endpoints.requests.public import GetPublicOEmbedRequest
from metabaseapi.endpoints.requests.public import GetPublicPivotCardQueryRequest
from metabaseapi.endpoints.requests.public import GetPublicPivotDashboardCardRequest
from metabaseapi.wire import QueryParamValue


def _parse_query_params(raw: str | None) -> dict[str, QueryParamValue]:
    return cast("dict[str, QueryParamValue]", parse_optional_json_object(raw, "params") or {})


@app.command("get-public-action")
def get_public_action(ctx: typer.Context, uuid: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, GetPublicActionRequest(uuid=uuid))


@app.command("execute-public-action")
def execute_public_action(
    ctx: typer.Context,
    uuid: str = typer.Argument(...),
    parameters: str | None = typer.Option(None, "--parameters", help="Execution parameters JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        ExecutePublicActionRequest(
            uuid=uuid,
            parameters=parse_optional_json_object_or_empty(parameters, "parameters"),
        ),
    )


@app.command("get-public-card")
def get_public_card(
    ctx: typer.Context,
    uuid: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Query parameters JSON object"),
) -> None:
    run_endpoint_command(ctx, GetPublicCardRequest(uuid=uuid, parameters=_parse_query_params(params)))


@app.command("get-public-card-param-remapping")
def get_public_card_param_remapping(
    ctx: typer.Context,
    uuid: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetPublicCardParamRemappingRequest(uuid=uuid, param_key=param_key, parameters=_parse_query_params(params)),
    )


@app.command("get-public-card-param-search")
def get_public_card_param_search(
    ctx: typer.Context,
    uuid: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    query: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetPublicCardParamSearchRequest(
            uuid=uuid,
            param_key=param_key,
            query=query,
            parameters=_parse_query_params(params),
        ),
    )


@app.command("get-public-card-param-values")
def get_public_card_param_values(
    ctx: typer.Context,
    uuid: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetPublicCardParamValuesRequest(uuid=uuid, param_key=param_key, parameters=_parse_query_params(params)),
    )


@app.command("get-public-card-query")
def get_public_card_query(
    ctx: typer.Context,
    uuid: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Query parameters JSON object"),
) -> None:
    run_endpoint_command(ctx, GetPublicCardQueryRequest(uuid=uuid, parameters=_parse_query_params(params)))


@app.command("get-public-card-query-export")
def get_public_card_query_export(
    ctx: typer.Context,
    uuid: str = typer.Argument(...),
    export_format: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Query parameters JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetPublicCardQueryExportRequest(uuid=uuid, export_format=export_format, parameters=_parse_query_params(params)),
    )


@app.command("get-public-dashboard")
def get_public_dashboard(
    ctx: typer.Context,
    uuid: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Query parameters JSON object"),
) -> None:
    run_endpoint_command(ctx, GetPublicDashboardRequest(uuid=uuid, parameters=_parse_query_params(params)))


@app.command("get-public-dashboard-card")
def get_public_dashboard_card(
    ctx: typer.Context,
    uuid: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    card_id: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Query parameters JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetPublicDashboardCardRequest(
            uuid=uuid,
            dashcard_id=dashcard_id,
            card_id=card_id,
            parameters=_parse_query_params(params),
        ),
    )


@app.command("export-public-dashboard-card")
def export_public_dashboard_card(
    ctx: typer.Context,
    uuid: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    card_id: str = typer.Argument(...),
    export_format: str = typer.Argument(...),
    body: str | None = typer.Argument(None, help="Optional query payload JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        ExportPublicDashboardCardRequest(
            uuid=uuid,
            dashcard_id=dashcard_id,
            card_id=card_id,
            export_format=export_format,
            body=parse_optional_json_object(body, "body"),
        ),
    )


@app.command("get-public-dashboard-dashcard-execute")
def get_public_dashboard_dashcard_execute(
    ctx: typer.Context,
    uuid: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Execution query parameters JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetPublicDashboardDashcardExecuteRequest(
            uuid=uuid,
            dashcard_id=dashcard_id,
            parameters=_parse_query_params(params),
        ),
    )


@app.command("execute-public-dashboard-dashcard")
def execute_public_dashboard_dashcard(
    ctx: typer.Context,
    uuid: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    parameters: str | None = typer.Option(None, "--parameters", help="Execution parameters JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        ExecutePublicDashboardDashcardRequest(
            uuid=uuid,
            dashcard_id=dashcard_id,
            parameters=parse_optional_json_object_or_empty(parameters, "parameters"),
        ),
    )


@app.command("get-public-dashboard-param-remapping")
def get_public_dashboard_param_remapping(
    ctx: typer.Context,
    uuid: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetPublicDashboardParamRemappingRequest(uuid=uuid, param_key=param_key, parameters=_parse_query_params(params)),
    )


@app.command("get-public-dashboard-param-search")
def get_public_dashboard_param_search(
    ctx: typer.Context,
    uuid: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    query: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetPublicDashboardParamSearchRequest(
            uuid=uuid,
            param_key=param_key,
            query=query,
            parameters=_parse_query_params(params),
        ),
    )


@app.command("get-public-dashboard-param-values")
def get_public_dashboard_param_values(
    ctx: typer.Context,
    uuid: str = typer.Argument(...),
    param_key: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Filter context JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetPublicDashboardParamValuesRequest(uuid=uuid, param_key=param_key, parameters=_parse_query_params(params)),
    )


@app.command("get-public-document")
def get_public_document(ctx: typer.Context, uuid: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, GetPublicDocumentRequest(uuid=uuid))


@app.command("get-public-document-card")
def get_public_document_card(
    ctx: typer.Context,
    uuid: str = typer.Argument(...),
    card_id: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Query parameters JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetPublicDocumentCardRequest(uuid=uuid, card_id=card_id, parameters=_parse_query_params(params)),
    )


@app.command("export-public-document-card")
def export_public_document_card(
    ctx: typer.Context,
    uuid: str = typer.Argument(...),
    card_id: str = typer.Argument(...),
    export_format: str = typer.Argument(...),
    body: str | None = typer.Argument(None, help="Optional query payload JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        ExportPublicDocumentCardRequest(
            uuid=uuid,
            card_id=card_id,
            export_format=export_format,
            body=parse_optional_json_object(body, "body"),
        ),
    )


@app.command("get-public-oembed")
def get_public_oembed(
    ctx: typer.Context,
    params: str | None = typer.Option(None, "--params", help="oEmbed query parameters JSON object"),
) -> None:
    run_endpoint_command(ctx, GetPublicOEmbedRequest(parameters=_parse_query_params(params)))


@app.command("get-public-pivot-card-query")
def get_public_pivot_card_query(
    ctx: typer.Context,
    uuid: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Query parameters JSON object"),
) -> None:
    run_endpoint_command(ctx, GetPublicPivotCardQueryRequest(uuid=uuid, parameters=_parse_query_params(params)))


@app.command("get-public-pivot-dashboard-card")
def get_public_pivot_dashboard_card(
    ctx: typer.Context,
    uuid: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    card_id: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Query parameters JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetPublicPivotDashboardCardRequest(
            uuid=uuid,
            dashcard_id=dashcard_id,
            card_id=card_id,
            parameters=_parse_query_params(params),
        ),
    )


@app.command("get-public-card-tile")
def get_public_card_tile(
    ctx: typer.Context,
    uuid: str = typer.Argument(...),
    zoom: str = typer.Argument(...),
    x: str = typer.Argument(...),
    y: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Tile query parameters JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetPublicCardTileRequest(uuid=uuid, zoom=zoom, x=x, y=y, parameters=_parse_query_params(params)),
    )


@app.command("get-public-dashboard-card-tile")
def get_public_dashboard_card_tile(
    ctx: typer.Context,
    uuid: str = typer.Argument(...),
    dashcard_id: str = typer.Argument(...),
    card_id: str = typer.Argument(...),
    zoom: str = typer.Argument(...),
    x: str = typer.Argument(...),
    y: str = typer.Argument(...),
    params: str | None = typer.Option(None, "--params", help="Tile query parameters JSON object"),
) -> None:
    run_endpoint_command(
        ctx,
        GetPublicDashboardCardTileRequest(
            uuid=uuid,
            dashcard_id=dashcard_id,
            card_id=card_id,
            zoom=zoom,
            x=x,
            y=y,
            parameters=_parse_query_params(params),
        ),
    )
