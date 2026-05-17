from __future__ import annotations

import typer

from metabaseapi.cli.runtime import _parse_json_object
from metabaseapi.cli.runtime import _run_and_print
from metabaseapi.cli.runtime import _run_client_call
from metabaseapi.cli.runtime import app
from metabaseapi.client.raw import activity as _raw_activity


@app.command("most-recently-viewed-dashboard")
def most_recently_viewed_dashboard(ctx: typer.Context) -> None:
    """Get the most recently viewed dashboard."""

    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: _raw_activity.most_recently_viewed_dashboard(
                client,
            ),
        )
    )


@app.command("list-popular-items")
def list_popular_items(ctx: typer.Context) -> None:
    """List popular items."""

    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: _raw_activity.list_popular_items(
                client,
            ),
        )
    )


@app.command("list-recent-views")
def list_recent_views(ctx: typer.Context) -> None:
    """List recent views."""

    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: _raw_activity.list_recent_views(
                client,
            ),
        )
    )


@app.command("list-recents")
def list_recents(ctx: typer.Context, context: str | None = typer.Option(None, "--context")) -> None:
    """List recents."""

    _run_and_print(_run_client_call(ctx, lambda client: _raw_activity.list_recents(client, context=context)))


@app.command("create-recent")
def create_recent(ctx: typer.Context, body: str = typer.Argument(..., help="Recent item JSON object")) -> None:
    """Add a recently selected item."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: _raw_activity.create_recent(client, payload)))
