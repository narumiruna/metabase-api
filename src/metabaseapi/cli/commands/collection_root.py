from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_json_object
from metabaseapi.cli.runtime import run_client_command
from metabaseapi.client.raw import collection_root as _raw_collection_root


@app.command("get-collection-root")
def get_collection_root(ctx: typer.Context) -> None:
    """Get the root collection."""

    run_client_command(
        ctx,
        lambda client: _raw_collection_root.get_collection_root(
            client,
        ),
    )


@app.command("get-collection-root-dashboard-question-candidates")
def get_collection_root_dashboard_question_candidates(ctx: typer.Context) -> None:
    """Find cards in root collection that can be moved into dashboards."""

    run_client_command(
        ctx,
        lambda client: _raw_collection_root.get_collection_root_dashboard_question_candidates(
            client,
        ),
    )


@app.command("get-collection-root-items")
def get_collection_root_items(ctx: typer.Context) -> None:
    """Fetch objects that the current user should see at root level."""

    run_client_command(
        ctx,
        lambda client: _raw_collection_root.get_collection_root_items(
            client,
        ),
    )


@app.command("post-collection-root-move-dashboard-question-candidates")
def post_collection_root_move_dashboard_question_candidates(
    ctx: typer.Context, body: str = typer.Argument(..., help="Collection root move payload JSON object")
) -> None:
    """Move candidate cards to dashboards they appear in."""

    payload = parse_json_object(body, "body")
    run_client_command(
        ctx,
        lambda client: _raw_collection_root.post_collection_root_move_dashboard_question_candidates(client, payload),
    )
