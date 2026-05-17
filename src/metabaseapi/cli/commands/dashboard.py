from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.dashboard import CopyDashboardRequest
from metabaseapi.endpoints.requests.dashboard import CreateDashboardPublicLinkRequest
from metabaseapi.endpoints.requests.dashboard import DeleteDashboardPublicLinkRequest
from metabaseapi.endpoints.requests.dashboard import DeleteDashboardRequest
from metabaseapi.endpoints.requests.dashboard import GetDashboardEmbeddableRequest
from metabaseapi.endpoints.requests.dashboard import GetDashboardItemsRequest
from metabaseapi.endpoints.requests.dashboard import GetDashboardPublicRequest
from metabaseapi.endpoints.requests.dashboard import GetDashboardRequest
from metabaseapi.endpoints.requests.dashboard import ListDashboardsRequest
from metabaseapi.endpoints.requests.dashboard import PostDashboardRequest
from metabaseapi.endpoints.requests.dashboard import SaveDashboardRequest
from metabaseapi.endpoints.requests.dashboard import SaveDashboardToCollectionRequest
from metabaseapi.endpoints.requests.dashboard import UpdateDashboardCardsRequest
from metabaseapi.endpoints.requests.dashboard import UpdateDashboardRequest


@app.command("list-dashboards")
def list_dashboards(ctx: typer.Context) -> None:
    """List dashboards."""

    run_endpoint_command(ctx, ListDashboardsRequest())


@app.command("create-dashboard")
def create_dashboard(ctx: typer.Context, body: str = typer.Argument(..., help="Dashboard body JSON object")) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: PostDashboardRequest(body=payload))


@app.command("save-dashboard")
def save_dashboard(ctx: typer.Context, body: str = typer.Argument(..., help="Dashboard save JSON object")) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: SaveDashboardRequest(body=payload))


@app.command("save-dashboard-to-collection")
def save_dashboard_to_collection(
    ctx: typer.Context,
    parent_collection_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Dashboard save JSON object"),
) -> None:
    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: SaveDashboardToCollectionRequest(parent_collection_id=parent_collection_id, body=payload),
    )


@app.command("get-dashboard")
def get_dashboard(ctx: typer.Context, dashboard_id: str = typer.Argument(...)) -> None:
    """Get a dashboard by ID."""

    run_endpoint_command(ctx, GetDashboardRequest(dashboard_id=dashboard_id))


@app.command("get-dashboard-embeddable")
def get_dashboard_embeddable(ctx: typer.Context) -> None:
    """List embeddable dashboards."""

    run_endpoint_command(ctx, GetDashboardEmbeddableRequest())


@app.command("get-dashboard-public")
def get_dashboard_public(ctx: typer.Context) -> None:
    """List public dashboards."""

    run_endpoint_command(ctx, GetDashboardPublicRequest())


@app.command("create-dashboard-public-link")
def create_dashboard_public_link(ctx: typer.Context, dashboard_id: str = typer.Argument(...)) -> None:
    """Create a public link for a dashboard."""

    run_endpoint_command(ctx, CreateDashboardPublicLinkRequest(dashboard_id=dashboard_id))


@app.command("delete-dashboard-public-link")
def delete_dashboard_public_link(ctx: typer.Context, dashboard_id: str = typer.Argument(...)) -> None:
    """Delete a public link for a dashboard."""

    run_endpoint_command(ctx, DeleteDashboardPublicLinkRequest(dashboard_id=dashboard_id))


@app.command("copy-dashboard")
def copy_dashboard(
    ctx: typer.Context,
    from_dashboard_id: str = typer.Argument(...),
    body: str | None = typer.Argument(None, help="Optional copy payload JSON object"),
) -> None:
    payload = parse_optional_json_object(body, "body") if body else None
    run_endpoint_command(ctx, CopyDashboardRequest(from_dashboard_id=from_dashboard_id, body=payload))


@app.command("delete-dashboard")
def delete_dashboard(ctx: typer.Context, dashboard_id: str = typer.Argument(...)) -> None:
    """Delete a dashboard."""

    run_endpoint_command(ctx, DeleteDashboardRequest(dashboard_id=dashboard_id))


@app.command("update-dashboard")
def update_dashboard(
    ctx: typer.Context, dashboard_id: str = typer.Argument(...), body: str = typer.Argument(...)
) -> None:
    run_json_body_endpoint_command(
        ctx, body, lambda payload: UpdateDashboardRequest(dashboard_id=dashboard_id, body=payload)
    )


@app.command("update-dashboard-cards")
def update_dashboard_cards(
    ctx: typer.Context,
    dashboard_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Dashboard cards JSON object"),
) -> None:
    run_json_body_endpoint_command(
        ctx, body, lambda payload: UpdateDashboardCardsRequest(dashboard_id=dashboard_id, body=payload)
    )


@app.command("get-dashboard-items")
def get_dashboard_items(ctx: typer.Context, dashboard_id: str = typer.Argument(...)) -> None:
    """Get dashboard items."""

    run_endpoint_command(ctx, GetDashboardItemsRequest(dashboard_id=dashboard_id))
