from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_json_object
from metabaseapi.cli.runtime import run_client_command
from metabaseapi.client.raw import collection as _raw_collection


@app.command("list-collections")
def list_collections(ctx: typer.Context) -> None:
    """List collections."""

    run_client_command(
        ctx,
        lambda client: _raw_collection.list_collections(
            client,
        ),
    )


@app.command("create-collection")
def create_collection(ctx: typer.Context, body: str = typer.Argument(..., help="Collection JSON object")) -> None:
    """Create a collection."""

    payload = parse_json_object(body, "body")
    run_client_command(ctx, lambda client: _raw_collection.create_collection(client, payload))


@app.command("get-collection")
def get_collection(ctx: typer.Context, collection_id: str = typer.Argument(...)) -> None:
    """Get a collection by ID."""

    run_client_command(ctx, lambda client: _raw_collection.get_collection(client, collection_id))


@app.command("update-collection")
def update_collection(
    ctx: typer.Context,
    collection_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Collection update payload JSON object"),
) -> None:
    """Update a collection."""

    payload = parse_json_object(body, "body")
    run_client_command(ctx, lambda client: _raw_collection.update_collection(client, collection_id, payload))


@app.command("delete-collection")
def delete_collection(ctx: typer.Context, collection_id: str = typer.Argument(...)) -> None:
    """Delete a collection."""

    run_client_command(ctx, lambda client: _raw_collection.delete_collection(client, collection_id))


@app.command("get-collection-dashboard-question-candidates")
def get_collection_dashboard_question_candidates(ctx: typer.Context, collection_id: str = typer.Argument(...)) -> None:
    """Find cards in a collection that can be moved into dashboards."""

    run_client_command(
        ctx,
        lambda client: _raw_collection.get_collection_dashboard_question_candidates(client, collection_id),
    )


@app.command("get-collection-items")
def get_collection_items(ctx: typer.Context, collection_id: str = typer.Argument(...)) -> None:
    """Fetch a collection's items."""

    run_client_command(ctx, lambda client: _raw_collection.get_collection_items(client, collection_id))


@app.command("post-collection-move-dashboard-question-candidates")
def post_collection_move_dashboard_question_candidates(
    ctx: typer.Context,
    collection_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Collection move payload JSON object"),
) -> None:
    """Move candidate cards to dashboards they appear in for a collection."""

    payload = parse_json_object(body, "body")
    run_client_command(
        ctx,
        lambda client: _raw_collection.post_collection_move_dashboard_question_candidates(
            client, collection_id, payload
        ),
    )


@app.command("get-collection-trash")
def get_collection_trash(ctx: typer.Context) -> None:
    """Fetch the trash collection."""

    run_client_command(
        ctx,
        lambda client: _raw_collection.get_collection_trash(
            client,
        ),
    )


@app.command("get-collection-tree")
def get_collection_tree(ctx: typer.Context) -> None:
    """Fetch collections in a tree structure."""

    run_client_command(
        ctx,
        lambda client: _raw_collection.get_collection_tree(
            client,
        ),
    )
