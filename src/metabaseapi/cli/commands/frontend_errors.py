from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.frontend_errors import ReportFrontendErrorRequest


@app.command("post-api-frontend-errors")
def post_api_frontend_errors(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Frontend error JSON object"),
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: ReportFrontendErrorRequest(body=payload))
