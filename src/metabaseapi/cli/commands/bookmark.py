from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.bookmark import CreateBookmarkRequest
from metabaseapi.endpoints.requests.bookmark import DeleteBookmarkRequest
from metabaseapi.endpoints.requests.bookmark import ListBookmarksRequest
from metabaseapi.endpoints.requests.bookmark import UpdateBookmarkOrderingRequest


@app.command("list-bookmarks")
def list_bookmarks(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, ListBookmarksRequest())


@app.command("update-bookmark-ordering")
def update_bookmark_ordering(
    ctx: typer.Context, body: str = typer.Argument(..., help="Bookmark ordering JSON object")
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateBookmarkOrderingRequest(body=payload))


@app.command("create-bookmark")
def create_bookmark(ctx: typer.Context, model: str = typer.Argument(...), item_id: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, CreateBookmarkRequest(model=model, item_id=item_id))


@app.command("delete-bookmark")
def delete_bookmark(ctx: typer.Context, model: str = typer.Argument(...), item_id: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, DeleteBookmarkRequest(model=model, item_id=item_id))
