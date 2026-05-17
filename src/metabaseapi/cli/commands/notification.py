from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.notification import CreateNotificationRequest
from metabaseapi.endpoints.requests.notification import GetNotificationRequest
from metabaseapi.endpoints.requests.notification import ListNotificationsRequest
from metabaseapi.endpoints.requests.notification import SendNotificationRequest
from metabaseapi.endpoints.requests.notification import SendUnsavedNotificationRequest
from metabaseapi.endpoints.requests.notification import UndoNotificationUnsubscribeRequest
from metabaseapi.endpoints.requests.notification import UnsubscribeNotificationByHashRequest
from metabaseapi.endpoints.requests.notification import UnsubscribeNotificationRequest
from metabaseapi.endpoints.requests.notification import UpdateNotificationRequest


@app.command("list-notifications")
def list_notifications(
    ctx: typer.Context,
    creator_id: str | None = typer.Option(None, "--creator-id"),
    recipient_id: str | None = typer.Option(None, "--recipient-id"),
) -> None:
    """List notifications."""

    run_endpoint_command(ctx, ListNotificationsRequest(creator_id=creator_id, recipient_id=recipient_id))


@app.command("create-notification")
def create_notification(ctx: typer.Context, body: str = typer.Argument(..., help="Notification JSON object")) -> None:
    """Create a notification."""

    run_json_body_endpoint_command(ctx, body, lambda payload: CreateNotificationRequest(body=payload))


@app.command("send-unsaved-notification")
def send_unsaved_notification(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Notification JSON object"),
) -> None:
    """Send an unsaved notification."""

    run_json_body_endpoint_command(ctx, body, lambda payload: SendUnsavedNotificationRequest(body=payload))


@app.command("get-notification")
def get_notification(ctx: typer.Context, notification_id: str = typer.Argument(..., help="Notification ID")) -> None:
    """Get a notification."""

    run_endpoint_command(ctx, GetNotificationRequest(notification_id=notification_id))


@app.command("update-notification")
def update_notification(
    ctx: typer.Context,
    notification_id: str = typer.Argument(..., help="Notification ID"),
    body: str = typer.Argument(..., help="Notification JSON object"),
) -> None:
    """Update a notification."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: UpdateNotificationRequest(notification_id=notification_id, body=payload),
    )


@app.command("send-notification")
def send_notification(ctx: typer.Context, notification_id: str = typer.Argument(..., help="Notification ID")) -> None:
    """Send a saved notification."""

    run_endpoint_command(ctx, SendNotificationRequest(notification_id=notification_id))


@app.command("unsubscribe-notification")
def unsubscribe_notification(
    ctx: typer.Context,
    notification_id: str = typer.Argument(..., help="Notification ID"),
) -> None:
    """Unsubscribe current user from a notification."""

    run_endpoint_command(ctx, UnsubscribeNotificationRequest(notification_id=notification_id))


@app.command("unsubscribe-notification-by-hash")
def unsubscribe_notification_by_hash(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Notification unsubscribe JSON object"),
) -> None:
    """Unsubscribe from a notification by email hash."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UnsubscribeNotificationByHashRequest(body=payload))


@app.command("undo-notification-unsubscribe")
def undo_notification_unsubscribe(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Notification unsubscribe undo JSON object"),
) -> None:
    """Undo a notification unsubscribe by email hash."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UndoNotificationUnsubscribeRequest(body=payload))
