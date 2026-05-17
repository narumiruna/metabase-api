from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_json_object
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.channel import CreateChannelRequest
from metabaseapi.endpoints.requests.channel import GetChannelRequest
from metabaseapi.endpoints.requests.channel import ListChannelsRequest
from metabaseapi.endpoints.requests.channel import TestChannelRequest
from metabaseapi.endpoints.requests.channel import UpdateChannelRequest


@app.command("list-channels")
def list_channels(ctx: typer.Context) -> None:
    """List notification channels."""

    run_endpoint_command(ctx, ListChannelsRequest())


@app.command("create-channel")
def create_channel(ctx: typer.Context, body: str = typer.Argument(..., help="Channel JSON object")) -> None:
    """Create a channel."""

    payload = parse_json_object(body, "body")
    run_endpoint_command(ctx, CreateChannelRequest(body=payload))


@app.command("test-channel")
def test_channel(ctx: typer.Context, body: str = typer.Argument(..., help="Channel JSON object")) -> None:
    """Test a channel connection."""

    payload = parse_json_object(body, "body")
    run_endpoint_command(ctx, TestChannelRequest(body=payload))


@app.command("get-channel")
def get_channel(ctx: typer.Context, channel_id: str = typer.Argument(..., help="Channel ID")) -> None:
    """Get a channel."""

    run_endpoint_command(ctx, GetChannelRequest(channel_id=channel_id))


@app.command("update-channel")
def update_channel(
    ctx: typer.Context,
    channel_id: str = typer.Argument(..., help="Channel ID"),
    body: str = typer.Argument(..., help="Channel JSON object"),
) -> None:
    """Update a channel."""

    payload = parse_json_object(body, "body")
    run_endpoint_command(ctx, UpdateChannelRequest(channel_id=channel_id, body=payload))
