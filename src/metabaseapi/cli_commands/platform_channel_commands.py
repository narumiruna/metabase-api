from __future__ import annotations

import typer

from metabaseapi.cli import _parse_json_object
from metabaseapi.cli import _run_and_print
from metabaseapi.cli import _run_client_call
from metabaseapi.cli import app


@app.command("list-channels")
def list_channels(ctx: typer.Context) -> None:
    """List notification channels."""

    _run_and_print(_run_client_call(ctx, lambda client: client.list_channels()))


@app.command("create-channel")
def create_channel(ctx: typer.Context, body: str = typer.Argument(..., help="Channel JSON object")) -> None:
    """Create a channel."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.create_channel(payload)))


@app.command("test-channel")
def test_channel(ctx: typer.Context, body: str = typer.Argument(..., help="Channel JSON object")) -> None:
    """Test a channel connection."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.test_channel(payload)))


@app.command("get-channel")
def get_channel(ctx: typer.Context, channel_id: str = typer.Argument(..., help="Channel ID")) -> None:
    """Get a channel."""

    _run_and_print(_run_client_call(ctx, lambda client: client.get_channel(channel_id)))


@app.command("update-channel")
def update_channel(
    ctx: typer.Context,
    channel_id: str = typer.Argument(..., help="Channel ID"),
    body: str = typer.Argument(..., help="Channel JSON object"),
) -> None:
    """Update a channel."""

    payload = _parse_json_object(body, "body")
    _run_and_print(_run_client_call(ctx, lambda client: client.update_channel(channel_id, payload)))
