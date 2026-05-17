from __future__ import annotations

import typer

from metabaseapi.cli.runtime import _parse_json_object
from metabaseapi.cli.runtime import _run_and_print
from metabaseapi.cli.runtime import _run_client_call
from metabaseapi.cli.runtime import app


@app.command("get-comment")
def get_comment(
    ctx: typer.Context,
    model: str | None = typer.Option(None, "--model"),
    model_id: str | None = typer.Option(None, "--model-id"),
) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_comment(model=model, model_id=model_id)))


@app.command("get-comment-mentions")
def get_comment_mentions(ctx: typer.Context) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_comment_mentions()))


@app.command("create-comment")
def create_comment(ctx: typer.Context, body: str = typer.Argument(..., help="Comment body JSON object")) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.create_comment(payload)))


@app.command("update-comment")
def update_comment(
    ctx: typer.Context, comment_id: str, body: str = typer.Argument(..., help="Comment body JSON object")
) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.update_comment(comment_id, payload)))


@app.command("post-comment-reaction")
def post_comment_reaction(
    ctx: typer.Context, comment_id: str, body: str = typer.Argument(..., help="Reaction body JSON object")
) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.post_comment_reaction(comment_id, payload)))


@app.command("delete-comment")
def delete_comment(ctx: typer.Context, comment_id: str = typer.Argument(...)) -> None:
    """Delete a comment."""

    _run_and_print(_run_client_call(ctx, lambda client: client.delete_comment(comment_id)))
