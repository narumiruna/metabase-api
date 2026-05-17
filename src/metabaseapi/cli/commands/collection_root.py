from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.collection_root import GetCollectionRootDashboardQuestionCandidatesRequest
from metabaseapi.endpoints.requests.collection_root import GetCollectionRootItemsRequest
from metabaseapi.endpoints.requests.collection_root import GetCollectionRootRequest
from metabaseapi.endpoints.requests.collection_root import PostCollectionRootMoveDashboardQuestionCandidatesRequest


@app.command("get-collection-root")
def get_collection_root(ctx: typer.Context) -> None:
    """Get the root collection."""

    run_endpoint_command(ctx, GetCollectionRootRequest())


@app.command("get-collection-root-dashboard-question-candidates")
def get_collection_root_dashboard_question_candidates(ctx: typer.Context) -> None:
    """Find cards in root collection that can be moved into dashboards."""

    run_endpoint_command(ctx, GetCollectionRootDashboardQuestionCandidatesRequest())


@app.command("get-collection-root-items")
def get_collection_root_items(ctx: typer.Context) -> None:
    """Fetch objects that the current user should see at root level."""

    run_endpoint_command(ctx, GetCollectionRootItemsRequest())


@app.command("post-collection-root-move-dashboard-question-candidates")
def post_collection_root_move_dashboard_question_candidates(
    ctx: typer.Context, body: str = typer.Argument(..., help="Collection root move payload JSON object")
) -> None:
    """Move candidate cards to dashboards they appear in."""

    run_json_body_endpoint_command(
        ctx, body, lambda payload: PostCollectionRootMoveDashboardQuestionCandidatesRequest(body=payload)
    )
