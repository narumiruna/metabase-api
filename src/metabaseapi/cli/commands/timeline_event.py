from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.timeline_event import CreateTimelineEventRequest
from metabaseapi.endpoints.requests.timeline_event import DeleteTimelineEventRequest
from metabaseapi.endpoints.requests.timeline_event import GetTimelineEventRequest
from metabaseapi.endpoints.requests.timeline_event import UpdateTimelineEventRequest


@app.command("create-timeline-event")
def create_timeline_event(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Timeline event JSON object"),
) -> None:
    """Create a timeline event."""

    run_json_body_endpoint_command(ctx, body, lambda payload: CreateTimelineEventRequest(body=payload))


@app.command("get-timeline-event")
def get_timeline_event(ctx: typer.Context, event_id: str = typer.Argument(...)) -> None:
    """Get a timeline event by ID."""

    run_endpoint_command(ctx, GetTimelineEventRequest(event_id=event_id))


@app.command("update-timeline-event")
def update_timeline_event(
    ctx: typer.Context,
    event_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Timeline event update payload JSON object"),
) -> None:
    """Update a timeline event."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: UpdateTimelineEventRequest(event_id=event_id, body=payload),
    )


@app.command("delete-timeline-event")
def delete_timeline_event(ctx: typer.Context, event_id: str = typer.Argument(...)) -> None:
    """Delete a timeline event."""

    run_endpoint_command(ctx, DeleteTimelineEventRequest(event_id=event_id))
