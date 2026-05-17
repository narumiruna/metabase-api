from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.pulse import CreatePulseRequest
from metabaseapi.endpoints.requests.pulse import DeletePulseSubscriptionRequest
from metabaseapi.endpoints.requests.pulse import GetPulseFormInputRequest
from metabaseapi.endpoints.requests.pulse import GetPulseRequest
from metabaseapi.endpoints.requests.pulse import ListPulsesRequest
from metabaseapi.endpoints.requests.pulse import TestPulseRequest
from metabaseapi.endpoints.requests.pulse import UndoPulseUnsubscribeRequest
from metabaseapi.endpoints.requests.pulse import UnsubscribePulseRequest
from metabaseapi.endpoints.requests.pulse import UpdatePulseRequest


@app.command("list-pulses")
def list_pulses(
    ctx: typer.Context,
    archived: bool | None = typer.Option(None, "--archived/--not-archived"),
    dashboard_id: str | None = typer.Option(None, "--dashboard-id"),
    creator_or_recipient: bool | None = typer.Option(None, "--creator-or-recipient/--not-creator-or-recipient"),
) -> None:
    """List dashboard subscriptions."""

    run_endpoint_command(
        ctx,
        ListPulsesRequest(
            archived=archived,
            dashboard_id=dashboard_id,
            creator_or_recipient=creator_or_recipient,
        ),
    )


@app.command("create-pulse")
def create_pulse(ctx: typer.Context, body: str = typer.Argument(..., help="Pulse JSON object")) -> None:
    """Create a pulse."""

    run_json_body_endpoint_command(ctx, body, lambda payload: CreatePulseRequest(body=payload))


@app.command("get-pulse-form-input")
def get_pulse_form_input(ctx: typer.Context) -> None:
    """Get pulse form input choices."""

    run_endpoint_command(ctx, GetPulseFormInputRequest())


@app.command("test-pulse")
def test_pulse(ctx: typer.Context, body: str = typer.Argument(..., help="Pulse JSON object")) -> None:
    """Test send an unsaved pulse."""

    run_json_body_endpoint_command(ctx, body, lambda payload: TestPulseRequest(body=payload))


@app.command("get-pulse")
def get_pulse(ctx: typer.Context, pulse_id: str = typer.Argument(..., help="Pulse ID")) -> None:
    """Get a pulse."""

    run_endpoint_command(ctx, GetPulseRequest(pulse_id=pulse_id))


@app.command("update-pulse")
def update_pulse(
    ctx: typer.Context,
    pulse_id: str = typer.Argument(..., help="Pulse ID"),
    body: str = typer.Argument(..., help="Pulse JSON object"),
) -> None:
    """Update a pulse."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UpdatePulseRequest(pulse_id=pulse_id, body=payload))


@app.command("delete-pulse-subscription")
def delete_pulse_subscription(ctx: typer.Context, pulse_id: str = typer.Argument(..., help="Pulse ID")) -> None:
    """Unsubscribe current user from a pulse subscription."""

    run_endpoint_command(ctx, DeletePulseSubscriptionRequest(pulse_id=pulse_id))


@app.command("unsubscribe-pulse")
def unsubscribe_pulse(ctx: typer.Context, body: str = typer.Argument(..., help="Unsubscribe JSON object")) -> None:
    """Unsubscribe from a pulse by email hash."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UnsubscribePulseRequest(body=payload))


@app.command("undo-pulse-unsubscribe")
def undo_pulse_unsubscribe(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Unsubscribe undo JSON object"),
) -> None:
    """Undo a pulse unsubscribe by email hash."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UndoPulseUnsubscribeRequest(body=payload))
