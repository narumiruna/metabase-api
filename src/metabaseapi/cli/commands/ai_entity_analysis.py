from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.ai_entity_analysis import AnalyzeChartRequest


@app.command("analyze-chart")
def analyze_chart(ctx: typer.Context, body: str = typer.Argument(..., help="Analyze chart JSON object")) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: AnalyzeChartRequest(body=payload))
