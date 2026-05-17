from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_json_object
from metabaseapi.cli.runtime import run_client_command
from metabaseapi.client.raw import ai_entity_analysis as _raw_ai_entity_analysis


@app.command("analyze-chart")
def analyze_chart(ctx: typer.Context, body: str = typer.Argument(..., help="Analyze chart JSON object")) -> None:
    payload = parse_json_object(body, "body")
    run_client_command(ctx, lambda client: _raw_ai_entity_analysis.analyze_chart(client, payload))
