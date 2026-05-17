from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.alert import DeleteAlertSubscriptionRequest
from metabaseapi.endpoints.requests.alert import GetAlertRequest
from metabaseapi.endpoints.requests.alert import ListAlertsRequest


@app.command("list-alerts")
def list_alerts(ctx: typer.Context, user_id: str | None = typer.Option(None, "--user-id")) -> None:
    run_endpoint_command(ctx, ListAlertsRequest(user_id=user_id))


@app.command("get-alert")
def get_alert(ctx: typer.Context, alert_id: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, GetAlertRequest(alert_id=alert_id))


@app.command("delete-alert-subscription")
def delete_alert_subscription(ctx: typer.Context, alert_id: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, DeleteAlertSubscriptionRequest(alert_id=alert_id))
