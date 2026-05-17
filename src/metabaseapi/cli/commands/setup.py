from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.setup import SetupRequest


@app.command("post-api-setup")
def post_api_setup(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Initial setup JSON object"),
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: SetupRequest(body=payload))
