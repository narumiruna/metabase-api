from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_json_object
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.analytics import CreateAnalyticsEventBatchRequest
from metabaseapi.endpoints.requests.analytics import GetAnonymousStatsRequest


@app.command("anonymous-stats")
def anonymous_stats(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, GetAnonymousStatsRequest())


@app.command("create-analytics-event-batch")
def create_analytics_event_batch(
    ctx: typer.Context, body: str = typer.Argument(..., help="Analytics event batch JSON object")
) -> None:
    payload = parse_json_object(body, "body")
    run_endpoint_command(ctx, CreateAnalyticsEventBatchRequest(body=payload))
