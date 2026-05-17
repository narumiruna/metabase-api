from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.logger import CreateLoggerAdjustmentRequest
from metabaseapi.endpoints.requests.logger import DeleteLoggerAdjustmentRequest
from metabaseapi.endpoints.requests.logger import GetLoggerLogsRequest
from metabaseapi.endpoints.requests.logger import GetLoggerPresetsRequest


@app.command("create-logger-adjustment")
def create_logger_adjustment(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Logger adjustment JSON object"),
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: CreateLoggerAdjustmentRequest(body=payload))


@app.command("delete-logger-adjustment")
def delete_logger_adjustment(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, DeleteLoggerAdjustmentRequest())


@app.command("get-logger-logs")
def get_logger_logs(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, GetLoggerLogsRequest())


@app.command("get-logger-presets")
def get_logger_presets(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, GetLoggerPresetsRequest())
