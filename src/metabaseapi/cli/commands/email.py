from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.email import DeleteEmailSettingsRequest
from metabaseapi.endpoints.requests.email import TestEmailRequest
from metabaseapi.endpoints.requests.email import UpdateEmailSettingsRequest


@app.command("update-email-settings")
def update_email_settings(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Email settings JSON object"),
) -> None:
    """Update email settings."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateEmailSettingsRequest(body=payload))


@app.command("delete-email-settings")
def delete_email_settings(ctx: typer.Context) -> None:
    """Clear email settings."""

    run_endpoint_command(ctx, DeleteEmailSettingsRequest())


@app.command("test-email")
def test_email(ctx: typer.Context, body: str = typer.Argument(..., help="Test email JSON object")) -> None:
    """Send a test email."""

    run_json_body_endpoint_command(ctx, body, lambda payload: TestEmailRequest(body=payload))
