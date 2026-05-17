from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_json_object
from metabaseapi.cli.runtime import run_client_command
from metabaseapi.client.raw import channel as _raw_channel


@app.command("list-channels")
def list_channels(ctx: typer.Context) -> None:
    """List notification channels."""

    run_client_command(
        ctx,
        lambda client: _raw_channel.list_channels(
            client,
        ),
    )


@app.command("create-channel")
def create_channel(ctx: typer.Context, body: str = typer.Argument(..., help="Channel JSON object")) -> None:
    """Create a channel."""

    payload = parse_json_object(body, "body")
    run_client_command(ctx, lambda client: _raw_channel.create_channel(client, payload))


@app.command("test-channel")
def test_channel(ctx: typer.Context, body: str = typer.Argument(..., help="Channel JSON object")) -> None:
    """Test a channel connection."""

    payload = parse_json_object(body, "body")
    run_client_command(ctx, lambda client: _raw_channel.test_channel(client, payload))


@app.command("get-channel")
def get_channel(ctx: typer.Context, channel_id: str = typer.Argument(..., help="Channel ID")) -> None:
    """Get a channel."""

    run_client_command(ctx, lambda client: _raw_channel.get_channel(client, channel_id))


@app.command("update-channel")
def update_channel(
    ctx: typer.Context,
    channel_id: str = typer.Argument(..., help="Channel ID"),
    body: str = typer.Argument(..., help="Channel JSON object"),
) -> None:
    """Update a channel."""

    payload = parse_json_object(body, "body")
    run_client_command(ctx, lambda client: _raw_channel.update_channel(client, channel_id, payload))
