from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_json_object
from metabaseapi.cli.runtime import run_client_command
from metabaseapi.client.raw import collection_graph as _raw_collection_graph


@app.command("get-collection-graph")
def get_collection_graph(ctx: typer.Context) -> None:
    """Fetch the collection permissions graph."""

    run_client_command(
        ctx,
        lambda client: _raw_collection_graph.get_collection_graph(
            client,
        ),
    )


@app.command("put-collection-graph")
def put_collection_graph(
    ctx: typer.Context, body: str = typer.Argument(..., help="Collection graph JSON object")
) -> None:
    """Update collection permissions via graph payload."""

    payload = parse_json_object(body, "body")
    run_client_command(ctx, lambda client: _raw_collection_graph.put_collection_graph(client, payload))
