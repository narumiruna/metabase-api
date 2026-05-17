from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_json_object
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.collection_graph import GetCollectionGraphRequest
from metabaseapi.endpoints.requests.collection_graph import PutCollectionGraphRequest


@app.command("get-collection-graph")
def get_collection_graph(ctx: typer.Context) -> None:
    """Fetch the collection permissions graph."""

    run_endpoint_command(ctx, GetCollectionGraphRequest())


@app.command("put-collection-graph")
def put_collection_graph(
    ctx: typer.Context, body: str = typer.Argument(..., help="Collection graph JSON object")
) -> None:
    """Update collection permissions via graph payload."""

    payload = parse_json_object(body, "body")
    run_endpoint_command(ctx, PutCollectionGraphRequest(body=payload))
