from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.ee_embedding_hub import GetEeEmbeddingHubChecklistRequest


@app.command("get-api-ee-embedding-hub-checklist")
def get_api_ee_embedding_hub_checklist(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, GetEeEmbeddingHubChecklistRequest())
