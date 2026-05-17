from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.ee_email import DeleteEeEmailOverrideRequest
from metabaseapi.endpoints.requests.ee_email import PutEeEmailOverrideRequest


@app.command("put-api-ee-email-override")
def put_api_ee_email_override(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Cloud email settings JSON object"),
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: PutEeEmailOverrideRequest(body=payload))


@app.command("delete-api-ee-email-override")
def delete_api_ee_email_override(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, DeleteEeEmailOverrideRequest())
