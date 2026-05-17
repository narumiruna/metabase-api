from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.collection import CreateCollectionRequest
from metabaseapi.endpoints.requests.collection import DeleteCollectionRequest
from metabaseapi.endpoints.requests.collection import GetCollectionDashboardQuestionCandidatesRequest
from metabaseapi.endpoints.requests.collection import GetCollectionItemsRequest
from metabaseapi.endpoints.requests.collection import GetCollectionRequest
from metabaseapi.endpoints.requests.collection import GetCollectionTrashRequest
from metabaseapi.endpoints.requests.collection import GetCollectionTreeRequest
from metabaseapi.endpoints.requests.collection import ListCollectionsRequest
from metabaseapi.endpoints.requests.collection import PostCollectionMoveDashboardQuestionCandidatesRequest
from metabaseapi.endpoints.requests.collection import PutCollectionRequest


@app.command("list-collections")
def list_collections(ctx: typer.Context) -> None:
    """List collections."""

    run_endpoint_command(ctx, ListCollectionsRequest())


@app.command("create-collection")
def create_collection(ctx: typer.Context, body: str = typer.Argument(..., help="Collection JSON object")) -> None:
    """Create a collection."""

    run_json_body_endpoint_command(ctx, body, lambda payload: CreateCollectionRequest(body=payload))


@app.command("get-collection")
def get_collection(ctx: typer.Context, collection_id: str = typer.Argument(...)) -> None:
    """Get a collection by ID."""

    run_endpoint_command(ctx, GetCollectionRequest(collection_id=collection_id))


@app.command("update-collection")
def update_collection(
    ctx: typer.Context,
    collection_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Collection update payload JSON object"),
) -> None:
    """Update a collection."""

    run_json_body_endpoint_command(
        ctx, body, lambda payload: PutCollectionRequest(collection_id=collection_id, body=payload)
    )


@app.command("delete-collection")
def delete_collection(ctx: typer.Context, collection_id: str = typer.Argument(...)) -> None:
    """Delete a collection."""

    run_endpoint_command(ctx, DeleteCollectionRequest(collection_id=collection_id))


@app.command("get-collection-dashboard-question-candidates")
def get_collection_dashboard_question_candidates(ctx: typer.Context, collection_id: str = typer.Argument(...)) -> None:
    """Find cards in a collection that can be moved into dashboards."""

    run_endpoint_command(ctx, GetCollectionDashboardQuestionCandidatesRequest(collection_id=collection_id))


@app.command("get-collection-items")
def get_collection_items(ctx: typer.Context, collection_id: str = typer.Argument(...)) -> None:
    """Fetch a collection's items."""

    run_endpoint_command(ctx, GetCollectionItemsRequest(collection_id=collection_id))


@app.command("post-collection-move-dashboard-question-candidates")
def post_collection_move_dashboard_question_candidates(
    ctx: typer.Context,
    collection_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Collection move payload JSON object"),
) -> None:
    """Move candidate cards to dashboards they appear in for a collection."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: PostCollectionMoveDashboardQuestionCandidatesRequest(collection_id=collection_id, body=payload),
    )


@app.command("get-collection-trash")
def get_collection_trash(ctx: typer.Context) -> None:
    """Fetch the trash collection."""

    run_endpoint_command(ctx, GetCollectionTrashRequest())


@app.command("get-collection-tree")
def get_collection_tree(ctx: typer.Context) -> None:
    """Fetch collections in a tree structure."""

    run_endpoint_command(ctx, GetCollectionTreeRequest())
