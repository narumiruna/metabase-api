from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.activity import CreateRecentRequest
from metabaseapi.endpoints.requests.activity import GetMostRecentlyViewedDashboardRequest
from metabaseapi.endpoints.requests.activity import ListPopularItemsRequest
from metabaseapi.endpoints.requests.activity import ListRecentsRequest
from metabaseapi.endpoints.requests.activity import ListRecentViewsRequest


@app.command("most-recently-viewed-dashboard")
def most_recently_viewed_dashboard(ctx: typer.Context) -> None:
    """Get the most recently viewed dashboard."""

    run_endpoint_command(ctx, GetMostRecentlyViewedDashboardRequest())


@app.command("list-popular-items")
def list_popular_items(ctx: typer.Context) -> None:
    """List popular items."""

    run_endpoint_command(ctx, ListPopularItemsRequest())


@app.command("list-recent-views")
def list_recent_views(ctx: typer.Context) -> None:
    """List recent views."""

    run_endpoint_command(ctx, ListRecentViewsRequest())


@app.command("list-recents")
def list_recents(ctx: typer.Context, context: str | None = typer.Option(None, "--context")) -> None:
    """List recents."""

    run_endpoint_command(ctx, ListRecentsRequest(context=context))


@app.command("create-recent")
def create_recent(ctx: typer.Context, body: str = typer.Argument(..., help="Recent item JSON object")) -> None:
    """Add a recently selected item."""

    run_json_body_endpoint_command(ctx, body, lambda payload: CreateRecentRequest(body=payload))
