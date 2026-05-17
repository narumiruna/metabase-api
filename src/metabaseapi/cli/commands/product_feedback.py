from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.product_feedback import CreateProductFeedbackRequest


@app.command("post-api-product-feedback")
def post_api_product_feedback(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Product feedback JSON object"),
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: CreateProductFeedbackRequest(body=payload))
