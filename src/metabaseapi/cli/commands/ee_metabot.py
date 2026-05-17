from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.ee_metabot import GetEeMetabotUsageRequest


@app.command("get-api-ee-metabot-usage")
def get_api_ee_metabot_usage(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, GetEeMetabotUsageRequest())
