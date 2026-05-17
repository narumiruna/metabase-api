from __future__ import annotations

import typer

from metabaseapi.cli import _parse_json_object
from metabaseapi.cli import _parse_optional_json_object
from metabaseapi.cli import _run_and_print
from metabaseapi.cli import _run_client_call
from metabaseapi.cli import app


@app.command("list-dashboards")
def list_dashboards(ctx: typer.Context) -> None:
    """List dashboards."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_dashboards()))


@app.command("create-dashboard")
def create_dashboard(ctx: typer.Context, body: str = typer.Argument(..., help="Dashboard body JSON object")) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.create_dashboard(payload)))


@app.command("save-dashboard")
def save_dashboard(ctx: typer.Context, body: str = typer.Argument(..., help="Dashboard save JSON object")) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.save_dashboard(payload)))


@app.command("save-dashboard-to-collection")
def save_dashboard_to_collection(
    ctx: typer.Context,
    parent_collection_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Dashboard save JSON object"),
) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(
        _run_client_call(ctx, lambda client: client.save_dashboard_to_collection(parent_collection_id, payload))
    )


@app.command("create-dashboard-public-link")
def create_dashboard_public_link(ctx: typer.Context, dashboard_id: str = typer.Argument(...)) -> None:
    """Create a public link for a dashboard."""

    _run_and_print(_run_client_call(ctx, lambda client: client.create_dashboard_public_link(dashboard_id)))


@app.command("delete-dashboard-public-link")
def delete_dashboard_public_link(ctx: typer.Context, dashboard_id: str = typer.Argument(...)) -> None:
    """Delete a public link for a dashboard."""

    _run_and_print(_run_client_call(ctx, lambda client: client.delete_dashboard_public_link(dashboard_id)))


@app.command("copy-dashboard")
def copy_dashboard(
    ctx: typer.Context,
    from_dashboard_id: str = typer.Argument(...),
    body: str | None = typer.Argument(None, help="Optional copy payload JSON object"),
) -> None:
    payload = _parse_optional_json_object(body, "body") if body else None
    _run_and_print(_run_client_call(ctx, lambda client: client.copy_dashboard(from_dashboard_id, payload)))


@app.command("delete-dashboard")
def delete_dashboard(ctx: typer.Context, dashboard_id: str = typer.Argument(...)) -> None:
    """Delete a dashboard."""

    _run_and_print(_run_client_call(ctx, lambda client: client.delete_dashboard(dashboard_id)))


@app.command("update-dashboard")
def update_dashboard(
    ctx: typer.Context, dashboard_id: str = typer.Argument(...), body: str = typer.Argument(...)
) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.update_dashboard(dashboard_id, payload)))


@app.command("update-dashboard-cards")
def update_dashboard_cards(
    ctx: typer.Context,
    dashboard_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Dashboard cards JSON object"),
) -> None:
    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.update_dashboard_cards(dashboard_id, payload)))


@app.command("get-dashboard-items")
def get_dashboard_items(ctx: typer.Context, dashboard_id: str = typer.Argument(...)) -> None:
    """Get dashboard items."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_dashboard_items(dashboard_id)))
