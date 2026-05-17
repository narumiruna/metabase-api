from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.timeline import CreateTimelineRequest
from metabaseapi.endpoints.requests.timeline import DeleteTimelineRequest
from metabaseapi.endpoints.requests.timeline import GetTimelineCollectionRequest
from metabaseapi.endpoints.requests.timeline import GetTimelineCollectionRootRequest
from metabaseapi.endpoints.requests.timeline import GetTimelineRequest
from metabaseapi.endpoints.requests.timeline import ListTimelinesRequest
from metabaseapi.endpoints.requests.timeline import UpdateTimelineRequest


@app.command("create-timeline")
def create_timeline(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Timeline JSON object"),
) -> None:
    """Create a timeline."""

    run_json_body_endpoint_command(ctx, body, lambda payload: CreateTimelineRequest(body=payload))


@app.command("list-timelines")
def list_timelines(
    ctx: typer.Context,
    include: str | None = typer.Option(None, "--include", help="Timeline include option, such as events"),
    archived: bool | None = typer.Option(None, "--archived/--no-archived"),
) -> None:
    """List timelines."""

    run_endpoint_command(ctx, ListTimelinesRequest(include=include, archived=archived))


@app.command("get-timeline-collection-root")
def get_timeline_collection_root(ctx: typer.Context) -> None:
    """Fetch root collection timelines."""

    run_endpoint_command(ctx, GetTimelineCollectionRootRequest())


@app.command("get-timeline-collection")
def get_timeline_collection(ctx: typer.Context, collection_id: str = typer.Argument(...)) -> None:
    """Fetch collection timelines."""

    run_endpoint_command(ctx, GetTimelineCollectionRequest(collection_id=collection_id))


@app.command("get-timeline")
def get_timeline(
    ctx: typer.Context,
    timeline_id: str = typer.Argument(...),
    include: str | None = typer.Option(None, "--include", help="Timeline include option, such as events"),
    archived: bool | None = typer.Option(None, "--archived/--no-archived"),
    start: str | None = typer.Option(None, "--start", help="Start date"),
    end: str | None = typer.Option(None, "--end", help="End date"),
) -> None:
    """Get a timeline by ID."""

    run_endpoint_command(
        ctx,
        GetTimelineRequest(timeline_id=timeline_id, include=include, archived=archived, start=start, end=end),
    )


@app.command("update-timeline")
def update_timeline(
    ctx: typer.Context,
    timeline_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Timeline update payload JSON object"),
) -> None:
    """Update a timeline."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: UpdateTimelineRequest(timeline_id=timeline_id, body=payload),
    )


@app.command("delete-timeline")
def delete_timeline(ctx: typer.Context, timeline_id: str = typer.Argument(...)) -> None:
    """Delete a timeline."""

    run_endpoint_command(ctx, DeleteTimelineRequest(timeline_id=timeline_id))
