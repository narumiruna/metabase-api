from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_json_body
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.setting import GetSettingRequest
from metabaseapi.endpoints.requests.setting import ListSettingsRequest
from metabaseapi.endpoints.requests.setting import UpdateSettingRequest
from metabaseapi.endpoints.requests.setting import UpdateSettingsRequest


@app.command("list-settings")
def list_settings(ctx: typer.Context) -> None:
    """Get all settings."""

    run_endpoint_command(ctx, ListSettingsRequest())


@app.command("update-settings")
def update_settings(ctx: typer.Context, body: str = typer.Argument(..., help="Settings JSON object")) -> None:
    """Update multiple settings."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateSettingsRequest(body=payload))


@app.command("get-setting")
def get_setting(ctx: typer.Context, key: str = typer.Argument(...)) -> None:
    """Fetch a single setting."""

    run_endpoint_command(ctx, GetSettingRequest(key=key))


@app.command("update-setting")
def update_setting(
    ctx: typer.Context,
    key: str = typer.Argument(...),
    value: str = typer.Argument(..., help="Setting value as JSON"),
) -> None:
    """Create, update, or delete a setting."""

    run_endpoint_command(ctx, UpdateSettingRequest(key=key, body=parse_json_body(value)))
