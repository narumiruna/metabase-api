from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.slack import CreateSlackBugReportRequest
from metabaseapi.endpoints.requests.slack import GetSlackAppInfoRequest
from metabaseapi.endpoints.requests.slack import GetSlackManifestRequest
from metabaseapi.endpoints.requests.slack import UpdateSlackSettingsRequest


@app.command("get-api-slack-app-info")
def get_api_slack_app_info(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, GetSlackAppInfoRequest())


@app.command("post-api-slack-bug-report")
def post_api_slack_bug_report(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Slack bug report JSON object"),
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: CreateSlackBugReportRequest(body=payload))


@app.command("get-api-slack-manifest")
def get_api_slack_manifest(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, GetSlackManifestRequest())


@app.command("put-api-slack-settings")
def put_api_slack_settings(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Slack settings JSON object"),
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateSlackSettingsRequest(body=payload))
