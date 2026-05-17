from __future__ import annotations

import typer

from metabaseapi.cli import _run_and_print
from metabaseapi.cli import _run_client_call
from metabaseapi.cli import app


@app.command("list-databases")
def list_databases(ctx: typer.Context) -> None:
    """List configured databases."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_databases()))


@app.command("list-cards")
def list_cards(ctx: typer.Context) -> None:
    """List cards."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_cards()))


@app.command("list-dashboards")
def list_dashboards(ctx: typer.Context) -> None:
    """List dashboards."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_dashboards()))


@app.command("list-users")
def list_users(ctx: typer.Context) -> None:
    """List users."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_users()))


@app.command("list-collections")
def list_collections(ctx: typer.Context) -> None:
    """List collections."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_collections()))


@app.command("list-tables")
def list_tables(ctx: typer.Context) -> None:
    """List tables."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_tables()))


@app.command("get-database")
def get_database(ctx: typer.Context, database_id: str = typer.Argument(...)) -> None:
    """Get a database by ID."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_database(database_id)))
