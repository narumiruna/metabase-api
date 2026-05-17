from __future__ import annotations

import typer

from metabaseapi.cli.runtime import _parse_json_object
from metabaseapi.cli.runtime import _run_and_print
from metabaseapi.cli.runtime import _run_client_call
from metabaseapi.cli.runtime import app
from metabaseapi.client.raw import analytics as _raw_analytics


@app.command("analyze-chart")
def analyze_chart(ctx: typer.Context, body: str = typer.Argument(..., help="Analyze chart JSON object")) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: _raw_analytics.analyze_chart(client, payload)))


@app.command("anonymous-stats")
def anonymous_stats(ctx: typer.Context) -> None:
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: _raw_analytics.anonymous_stats(
                client,
            ),
        )
    )


@app.command("create-analytics-event-batch")
def create_analytics_event_batch(
    ctx: typer.Context, body: str = typer.Argument(..., help="Analytics event batch JSON object")
) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: _raw_analytics.create_analytics_event_batch(client, payload)))
