from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_json_object
from metabaseapi.cli.runtime import run_client_command
from metabaseapi.client.raw import bookmark as _raw_bookmark


@app.command("list-bookmarks")
def list_bookmarks(ctx: typer.Context) -> None:
    run_client_command(
        ctx,
        lambda client: _raw_bookmark.list_bookmarks(
            client,
        ),
    )


@app.command("update-bookmark-ordering")
def update_bookmark_ordering(
    ctx: typer.Context, body: str = typer.Argument(..., help="Bookmark ordering JSON object")
) -> None:
    payload = parse_json_object(body, "body")
    run_client_command(ctx, lambda client: _raw_bookmark.update_bookmark_ordering(client, payload))


@app.command("create-bookmark")
def create_bookmark(ctx: typer.Context, model: str = typer.Argument(...), item_id: str = typer.Argument(...)) -> None:
    run_client_command(ctx, lambda client: _raw_bookmark.create_bookmark(client, model, item_id))


@app.command("delete-bookmark")
def delete_bookmark(ctx: typer.Context, model: str = typer.Argument(...), item_id: str = typer.Argument(...)) -> None:
    run_client_command(ctx, lambda client: _raw_bookmark.delete_bookmark(client, model, item_id))
