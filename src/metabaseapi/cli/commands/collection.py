from __future__ import annotations

import typer

from metabaseapi.cli.runtime import _parse_json_object
from metabaseapi.cli.runtime import _run_and_print
from metabaseapi.cli.runtime import _run_client_call
from metabaseapi.cli.runtime import app


@app.command("list-collections")
def list_collections(ctx: typer.Context) -> None:
    """List collections."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_collections()))


@app.command("create-collection")
def create_collection(ctx: typer.Context, body: str = typer.Argument(..., help="Collection JSON object")) -> None:
    """Create a collection."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.create_collection(payload)))


@app.command("get-collection")
def get_collection(ctx: typer.Context, collection_id: str = typer.Argument(...)) -> None:
    """Get a collection by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_collection(collection_id)))


@app.command("update-collection")
def update_collection(
    ctx: typer.Context,
    collection_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Collection update payload JSON object"),
) -> None:
    """Update a collection."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.update_collection(collection_id, payload)))


@app.command("delete-collection")
def delete_collection(ctx: typer.Context, collection_id: str = typer.Argument(...)) -> None:
    """Delete a collection."""

    _run_and_print(_run_client_call(ctx, lambda client: client.delete_collection(collection_id)))


@app.command("get-collection-dashboard-question-candidates")
def get_collection_dashboard_question_candidates(ctx: typer.Context, collection_id: str = typer.Argument(...)) -> None:
    """Find cards in a collection that can be moved into dashboards."""

    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.get_collection_dashboard_question_candidates(collection_id),
        )
    )


@app.command("get-collection-items")
def get_collection_items(ctx: typer.Context, collection_id: str = typer.Argument(...)) -> None:
    """Fetch a collection's items."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_collection_items(collection_id)))


@app.command("get-collection-root")
def get_collection_root(ctx: typer.Context) -> None:
    """Get the root collection."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_collection_root()))


@app.command("get-collection-root-dashboard-question-candidates")
def get_collection_root_dashboard_question_candidates(ctx: typer.Context) -> None:
    """Find cards in root collection that can be moved into dashboards."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_collection_root_dashboard_question_candidates()))


@app.command("get-collection-root-items")
def get_collection_root_items(ctx: typer.Context) -> None:
    """Fetch objects that the current user should see at root level."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_collection_root_items()))


@app.command("post-collection-root-move-dashboard-question-candidates")
def post_collection_root_move_dashboard_question_candidates(
    ctx: typer.Context, body: str = typer.Argument(..., help="Collection root move payload JSON object")
) -> None:
    """Move candidate cards to dashboards they appear in."""

    payload = _parse_json_object(body, "body")
    _run_and_print(
        _run_client_call(ctx, lambda client: client.post_collection_root_move_dashboard_question_candidates(payload))
    )


@app.command("post-collection-move-dashboard-question-candidates")
def post_collection_move_dashboard_question_candidates(
    ctx: typer.Context,
    collection_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Collection move payload JSON object"),
) -> None:
    """Move candidate cards to dashboards they appear in for a collection."""

    payload = _parse_json_object(body, "body")
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.post_collection_move_dashboard_question_candidates(collection_id, payload),
        )
    )


@app.command("get-collection-trash")
def get_collection_trash(ctx: typer.Context) -> None:
    """Fetch the trash collection."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_collection_trash()))


@app.command("get-collection-tree")
def get_collection_tree(ctx: typer.Context) -> None:
    """Fetch collections in a tree structure."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_collection_tree()))


@app.command("get-collection-graph")
def get_collection_graph(ctx: typer.Context) -> None:
    """Fetch the collection permissions graph."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_collection_graph()))


@app.command("put-collection-graph")
def put_collection_graph(
    ctx: typer.Context, body: str = typer.Argument(..., help="Collection graph JSON object")
) -> None:
    """Update collection permissions via graph payload."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.put_collection_graph(payload)))
