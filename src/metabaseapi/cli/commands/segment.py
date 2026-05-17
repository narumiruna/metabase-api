from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.segment import CreateSegmentRequest
from metabaseapi.endpoints.requests.segment import DeleteSegmentRequest
from metabaseapi.endpoints.requests.segment import GetSegmentRelatedRequest
from metabaseapi.endpoints.requests.segment import GetSegmentRequest
from metabaseapi.endpoints.requests.segment import ListSegmentsRequest
from metabaseapi.endpoints.requests.segment import UpdateSegmentRequest


@app.command("create-segment")
def create_segment(ctx: typer.Context, body: str = typer.Argument(..., help="Segment JSON object")) -> None:
    """Create a segment."""

    run_json_body_endpoint_command(ctx, body, lambda payload: CreateSegmentRequest(body=payload))


@app.command("list-segments")
def list_segments(ctx: typer.Context) -> None:
    """List segments."""

    run_endpoint_command(ctx, ListSegmentsRequest())


@app.command("get-segment")
def get_segment(ctx: typer.Context, segment_id: str = typer.Argument(...)) -> None:
    """Get a segment by ID."""

    run_endpoint_command(ctx, GetSegmentRequest(segment_id=segment_id))


@app.command("update-segment")
def update_segment(
    ctx: typer.Context,
    segment_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Segment update JSON object"),
) -> None:
    """Update a segment."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateSegmentRequest(segment_id=segment_id, body=payload))


@app.command("delete-segment")
def delete_segment(ctx: typer.Context, segment_id: str = typer.Argument(...)) -> None:
    """Archive a segment."""

    run_endpoint_command(ctx, DeleteSegmentRequest(segment_id=segment_id))


@app.command("get-segment-related")
def get_segment_related(ctx: typer.Context, segment_id: str = typer.Argument(...)) -> None:
    """Get entities related to a segment."""

    run_endpoint_command(ctx, GetSegmentRelatedRequest(segment_id=segment_id))
