from __future__ import annotations

from typing import Annotated
from typing import cast

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object_or_empty
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.search import ForceSearchReindexRequest
from metabaseapi.endpoints.requests.search import GetSearchWeightsRequest
from metabaseapi.endpoints.requests.search import ReInitSearchRequest
from metabaseapi.endpoints.requests.search import SearchRequest
from metabaseapi.endpoints.requests.search import UpdateSearchWeightsRequest
from metabaseapi.wire import QueryParamValue


@app.command("search")
def search(
    ctx: typer.Context,
    q: Annotated[str | None, typer.Option("--q")] = None,
    archived: Annotated[bool | None, typer.Option("--archived/--not-archived")] = None,
    model: Annotated[list[str] | None, typer.Option("--model")] = None,
    table_db_id: Annotated[str | None, typer.Option("--table-db-id")] = None,
    collection_id: Annotated[str | None, typer.Option("--collection-id")] = None,
    creator_id: Annotated[str | None, typer.Option("--creator-id")] = None,
    verified: Annotated[bool | None, typer.Option("--verified/--not-verified")] = None,
    include_dashboard_questions: Annotated[
        bool | None,
        typer.Option("--include-dashboard-questions/--exclude-dashboard-questions"),
    ] = None,
    search_native_query: Annotated[bool | None, typer.Option("--search-native-query/--no-search-native-query")] = None,
    context: Annotated[str | None, typer.Option("--context")] = None,
    namespace: Annotated[str | None, typer.Option("--namespace")] = None,
    limit: Annotated[int | None, typer.Option("--limit")] = None,
    offset: Annotated[int | None, typer.Option("--offset")] = None,
    extra_params: Annotated[
        str | None,
        typer.Option("--extra-params", help="Additional query params JSON object"),
    ] = None,
) -> None:
    """Search for Metabase items."""

    run_endpoint_command(
        ctx,
        SearchRequest(
            q=q,
            archived=archived,
            models=model,
            table_db_id=table_db_id,
            collection_id=collection_id,
            creator_id=creator_id,
            verified=verified,
            include_dashboard_questions=include_dashboard_questions,
            search_native_query=search_native_query,
            context=context,
            namespace=namespace,
            limit=limit,
            offset=offset,
            extra_params=cast(
                "dict[str, QueryParamValue]",
                parse_optional_json_object_or_empty(extra_params, "extra_params"),
            ),
        ),
    )


@app.command("force-search-reindex")
def force_search_reindex(ctx: typer.Context) -> None:
    """Trigger immediate search reindexing."""

    run_endpoint_command(ctx, ForceSearchReindexRequest())


@app.command("re-init-search")
def re_init_search(ctx: typer.Context) -> None:
    """Re-create and re-populate search indexes."""

    run_endpoint_command(ctx, ReInitSearchRequest())


@app.command("get-search-weights")
def get_search_weights(ctx: typer.Context) -> None:
    """Get search ranking weights."""

    run_endpoint_command(ctx, GetSearchWeightsRequest())


@app.command("update-search-weights")
def update_search_weights(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Search weights JSON object"),
) -> None:
    """Update search ranking weights."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateSearchWeightsRequest(body=payload))
