from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.comment import DeleteCommentRequest
from metabaseapi.endpoints.requests.comment import GetCommentMentionsRequest
from metabaseapi.endpoints.requests.comment import GetCommentRequest
from metabaseapi.endpoints.requests.comment import PostCommentReactionRequest
from metabaseapi.endpoints.requests.comment import PostCommentRequest
from metabaseapi.endpoints.requests.comment import UpdateCommentRequest


@app.command("get-comment")
def get_comment(
    ctx: typer.Context,
    model: str | None = typer.Option(None, "--model"),
    model_id: str | None = typer.Option(None, "--model-id"),
) -> None:
    run_endpoint_command(ctx, GetCommentRequest(model=model, model_id=model_id))


@app.command("get-comment-mentions")
def get_comment_mentions(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, GetCommentMentionsRequest())


@app.command("create-comment")
def create_comment(ctx: typer.Context, body: str = typer.Argument(..., help="Comment body JSON object")) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: PostCommentRequest(body=payload))


@app.command("update-comment")
def update_comment(
    ctx: typer.Context, comment_id: str, body: str = typer.Argument(..., help="Comment body JSON object")
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateCommentRequest(comment_id=comment_id, body=payload))


@app.command("post-comment-reaction")
def post_comment_reaction(
    ctx: typer.Context, comment_id: str, body: str = typer.Argument(..., help="Reaction body JSON object")
) -> None:
    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: PostCommentReactionRequest(comment_id=comment_id, body=payload),
    )


@app.command("delete-comment")
def delete_comment(ctx: typer.Context, comment_id: str = typer.Argument(...)) -> None:
    """Delete a comment."""

    run_endpoint_command(ctx, DeleteCommentRequest(comment_id=comment_id))
