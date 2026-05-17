from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.google import UpdateGoogleSettingsRequest


@app.command("put-api-google-settings")
def put_api_google_settings(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Google settings JSON object"),
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateGoogleSettingsRequest(body=payload))
