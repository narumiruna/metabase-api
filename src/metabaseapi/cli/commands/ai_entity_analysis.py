from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_json_object
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.ai_entity_analysis import AnalyzeChartRequest


@app.command("analyze-chart")
def analyze_chart(ctx: typer.Context, body: str = typer.Argument(..., help="Analyze chart JSON object")) -> None:
    payload = parse_json_object(body, "body")
    run_endpoint_command(ctx, AnalyzeChartRequest(body=payload))
