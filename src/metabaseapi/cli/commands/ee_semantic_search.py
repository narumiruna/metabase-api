from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.ee_semantic_search import GetEeSemanticSearchStatusRequest


@app.command("get-api-ee-semantic-search-status")
def get_api_ee_semantic_search_status(ctx: typer.Context) -> None:
    """Fetch the active semantic search index status."""

    run_endpoint_command(ctx, GetEeSemanticSearchStatusRequest())
