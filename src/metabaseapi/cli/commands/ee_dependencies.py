from __future__ import annotations

from typing import Annotated
from typing import cast

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object_or_empty
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.ee_dependencies import CheckEeDependenciesCardRequest
from metabaseapi.endpoints.requests.ee_dependencies import CheckEeDependenciesSnippetRequest
from metabaseapi.endpoints.requests.ee_dependencies import CheckEeDependenciesTransformRequest
from metabaseapi.endpoints.requests.ee_dependencies import GetEeDependenciesBackfillStatusRequest
from metabaseapi.endpoints.requests.ee_dependencies import GetEeDependenciesGraphBreakingRequest
from metabaseapi.endpoints.requests.ee_dependencies import GetEeDependenciesGraphBrokenRequest
from metabaseapi.endpoints.requests.ee_dependencies import GetEeDependenciesGraphDependentsRequest
from metabaseapi.endpoints.requests.ee_dependencies import GetEeDependenciesGraphRequest
from metabaseapi.endpoints.requests.ee_dependencies import GetEeDependenciesGraphUnreferencedRequest
from metabaseapi.wire import QueryParamValue


def _extra_params(raw: str | None) -> dict[str, QueryParamValue]:
    return cast("dict[str, QueryParamValue]", parse_optional_json_object_or_empty(raw, "extra_params"))


@app.command("get-api-ee-dependencies-backfill-status")
def get_api_ee_dependencies_backfill_status(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, GetEeDependenciesBackfillStatusRequest())


@app.command("post-api-ee-dependencies-check-card")
def post_api_ee_dependencies_check_card(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Card edit JSON object"),
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: CheckEeDependenciesCardRequest(body=payload))


@app.command("post-api-ee-dependencies-check-snippet")
def post_api_ee_dependencies_check_snippet(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Snippet edit JSON object"),
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: CheckEeDependenciesSnippetRequest(body=payload))


@app.command("post-api-ee-dependencies-check-transform")
def post_api_ee_dependencies_check_transform(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Transform edit JSON object"),
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: CheckEeDependenciesTransformRequest(body=payload))


@app.command("get-api-ee-dependencies-graph")
def get_api_ee_dependencies_graph(
    ctx: typer.Context,
    entity_id: Annotated[str, typer.Option("--id")],
    entity_type: Annotated[str, typer.Option("--type")],
    extra_params: Annotated[
        str | None,
        typer.Option("--extra-params", help="Additional query params JSON object"),
    ] = None,
) -> None:
    run_endpoint_command(
        ctx,
        GetEeDependenciesGraphRequest(
            entity_id=entity_id,
            entity_type=entity_type,
            extra_params=_extra_params(extra_params),
        ),
    )


@app.command("get-api-ee-dependencies-graph-breaking")
def get_api_ee_dependencies_graph_breaking(
    ctx: typer.Context,
    extra_params: Annotated[
        str | None,
        typer.Option("--extra-params", help="Additional query params JSON object"),
    ] = None,
) -> None:
    run_endpoint_command(ctx, GetEeDependenciesGraphBreakingRequest(extra_params=_extra_params(extra_params)))


@app.command("get-api-ee-dependencies-graph-broken")
def get_api_ee_dependencies_graph_broken(
    ctx: typer.Context,
    entity_id: Annotated[str, typer.Option("--id")],
    entity_type: Annotated[str, typer.Option("--type")],
    extra_params: Annotated[
        str | None,
        typer.Option("--extra-params", help="Additional query params JSON object"),
    ] = None,
) -> None:
    run_endpoint_command(
        ctx,
        GetEeDependenciesGraphBrokenRequest(
            entity_id=entity_id,
            entity_type=entity_type,
            extra_params=_extra_params(extra_params),
        ),
    )


@app.command("get-api-ee-dependencies-graph-dependents")
def get_api_ee_dependencies_graph_dependents(
    ctx: typer.Context,
    entity_id: Annotated[str, typer.Option("--id")],
    entity_type: Annotated[str, typer.Option("--type")],
    extra_params: Annotated[
        str | None,
        typer.Option("--extra-params", help="Additional query params JSON object"),
    ] = None,
) -> None:
    run_endpoint_command(
        ctx,
        GetEeDependenciesGraphDependentsRequest(
            entity_id=entity_id,
            entity_type=entity_type,
            extra_params=_extra_params(extra_params),
        ),
    )


@app.command("get-api-ee-dependencies-graph-unreferenced")
def get_api_ee_dependencies_graph_unreferenced(
    ctx: typer.Context,
    entity_type: Annotated[str | None, typer.Option("--type")] = None,
    extra_params: Annotated[
        str | None,
        typer.Option("--extra-params", help="Additional query params JSON object"),
    ] = None,
) -> None:
    run_endpoint_command(
        ctx,
        GetEeDependenciesGraphUnreferencedRequest(entity_type=entity_type, extra_params=_extra_params(extra_params)),
    )
