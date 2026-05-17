from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.ee_data_complexity_score import GetEeDataComplexityScoreComplexityRequest


@app.command("get-ee-data-complexity-score-complexity")
def get_ee_data_complexity_score_complexity(ctx: typer.Context) -> None:
    """Fetch the EE data complexity score."""

    run_endpoint_command(ctx, GetEeDataComplexityScoreComplexityRequest())
