from __future__ import annotations

import typer

from metabaseapi.cli import _parse_json_object
from metabaseapi.cli import _run_and_print
from metabaseapi.cli import _run_client_call
from metabaseapi.cli import app


@app.command("analyze-chart")
def analyze_chart(ctx: typer.Context, body: str = typer.Argument(..., help="Analyze chart JSON object")) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.analyze_chart(payload)))


@app.command("anonymous-stats")
def anonymous_stats(ctx: typer.Context) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.anonymous_stats()))


@app.command("create-analytics-event-batch")
def create_analytics_event_batch(
    ctx: typer.Context, body: str = typer.Argument(..., help="Analytics event batch JSON object")
) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.create_analytics_event_batch(payload)))
