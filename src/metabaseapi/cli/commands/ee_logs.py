from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.ee_logs import GetEeLogsQueryExecutionRequest


@app.command("get-api-ee-logs-query_execution-yyyy-mm")
def get_api_ee_logs_query_execution_yyyy_mm(
    ctx: typer.Context,
    year_month: str = typer.Argument(..., help="Month in YYYY-MM format"),
) -> None:
    run_endpoint_command(ctx, GetEeLogsQueryExecutionRequest(year_month=year_month))
