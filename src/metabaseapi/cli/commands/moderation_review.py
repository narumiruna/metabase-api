from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.moderation_review import CreateModerationReviewRequest


@app.command("post-api-moderation-review")
def post_api_moderation_review(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Moderation review JSON object"),
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: CreateModerationReviewRequest(body=payload))
