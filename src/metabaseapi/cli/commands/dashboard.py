from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_json_object
from metabaseapi.cli.runtime import parse_optional_json_object
from metabaseapi.cli.runtime import run_client_command
from metabaseapi.client.raw import dashboard as _raw_dashboard


@app.command("list-dashboards")
def list_dashboards(ctx: typer.Context) -> None:
    """List dashboards."""

    run_client_command(
        ctx,
        lambda client: _raw_dashboard.list_dashboards(
            client,
        ),
    )


@app.command("create-dashboard")
def create_dashboard(ctx: typer.Context, body: str = typer.Argument(..., help="Dashboard body JSON object")) -> None:
    payload = parse_json_object(body, "body")
    run_client_command(ctx, lambda client: _raw_dashboard.create_dashboard(client, payload))


@app.command("save-dashboard")
def save_dashboard(ctx: typer.Context, body: str = typer.Argument(..., help="Dashboard save JSON object")) -> None:
    payload = parse_json_object(body, "body")
    run_client_command(ctx, lambda client: _raw_dashboard.save_dashboard(client, payload))


@app.command("save-dashboard-to-collection")
def save_dashboard_to_collection(
    ctx: typer.Context,
    parent_collection_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Dashboard save JSON object"),
) -> None:
    payload = parse_json_object(body, "body")
    run_client_command(
        ctx, lambda client: _raw_dashboard.save_dashboard_to_collection(client, parent_collection_id, payload)
    )


@app.command("create-dashboard-public-link")
def create_dashboard_public_link(ctx: typer.Context, dashboard_id: str = typer.Argument(...)) -> None:
    """Create a public link for a dashboard."""

    run_client_command(ctx, lambda client: _raw_dashboard.create_dashboard_public_link(client, dashboard_id))


@app.command("delete-dashboard-public-link")
def delete_dashboard_public_link(ctx: typer.Context, dashboard_id: str = typer.Argument(...)) -> None:
    """Delete a public link for a dashboard."""

    run_client_command(ctx, lambda client: _raw_dashboard.delete_dashboard_public_link(client, dashboard_id))


@app.command("copy-dashboard")
def copy_dashboard(
    ctx: typer.Context,
    from_dashboard_id: str = typer.Argument(...),
    body: str | None = typer.Argument(None, help="Optional copy payload JSON object"),
) -> None:
    payload = parse_optional_json_object(body, "body") if body else None
    run_client_command(ctx, lambda client: _raw_dashboard.copy_dashboard(client, from_dashboard_id, payload))


@app.command("delete-dashboard")
def delete_dashboard(ctx: typer.Context, dashboard_id: str = typer.Argument(...)) -> None:
    """Delete a dashboard."""

    run_client_command(ctx, lambda client: _raw_dashboard.delete_dashboard(client, dashboard_id))


@app.command("update-dashboard")
def update_dashboard(
    ctx: typer.Context, dashboard_id: str = typer.Argument(...), body: str = typer.Argument(...)
) -> None:
    payload = parse_json_object(body, "body")
    run_client_command(ctx, lambda client: _raw_dashboard.update_dashboard(client, dashboard_id, payload))


@app.command("update-dashboard-cards")
def update_dashboard_cards(
    ctx: typer.Context,
    dashboard_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Dashboard cards JSON object"),
) -> None:
    payload = parse_json_object(body, "body")
    run_client_command(ctx, lambda client: _raw_dashboard.update_dashboard_cards(client, dashboard_id, payload))


@app.command("get-dashboard-items")
def get_dashboard_items(ctx: typer.Context, dashboard_id: str = typer.Argument(...)) -> None:
    """Get dashboard items."""

    run_client_command(ctx, lambda client: _raw_dashboard.get_dashboard_items(client, dashboard_id))
