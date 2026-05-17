from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_json_object
from metabaseapi.cli.runtime import run_client_command
from metabaseapi.client.raw import comment as _raw_comment


@app.command("get-comment")
def get_comment(
    ctx: typer.Context,
    model: str | None = typer.Option(None, "--model"),
    model_id: str | None = typer.Option(None, "--model-id"),
) -> None:
    run_client_command(ctx, lambda client: _raw_comment.get_comment(client, model=model, model_id=model_id))


@app.command("get-comment-mentions")
def get_comment_mentions(ctx: typer.Context) -> None:
    run_client_command(
        ctx,
        lambda client: _raw_comment.get_comment_mentions(
            client,
        ),
    )


@app.command("create-comment")
def create_comment(ctx: typer.Context, body: str = typer.Argument(..., help="Comment body JSON object")) -> None:
    payload = parse_json_object(body, "body")
    run_client_command(ctx, lambda client: _raw_comment.create_comment(client, payload))


@app.command("update-comment")
def update_comment(
    ctx: typer.Context, comment_id: str, body: str = typer.Argument(..., help="Comment body JSON object")
) -> None:
    payload = parse_json_object(body, "body")
    run_client_command(ctx, lambda client: _raw_comment.update_comment(client, comment_id, payload))


@app.command("post-comment-reaction")
def post_comment_reaction(
    ctx: typer.Context, comment_id: str, body: str = typer.Argument(..., help="Reaction body JSON object")
) -> None:
    payload = parse_json_object(body, "body")
    run_client_command(ctx, lambda client: _raw_comment.post_comment_reaction(client, comment_id, payload))


@app.command("delete-comment")
def delete_comment(ctx: typer.Context, comment_id: str = typer.Argument(...)) -> None:
    """Delete a comment."""

    run_client_command(ctx, lambda client: _raw_comment.delete_comment(client, comment_id))
