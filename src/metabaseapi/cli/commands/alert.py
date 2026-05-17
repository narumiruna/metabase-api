from __future__ import annotations

import typer

from metabaseapi.cli.runtime import _run_and_print
from metabaseapi.cli.runtime import _run_client_call
from metabaseapi.cli.runtime import app


@app.command("list-alerts")
def list_alerts(ctx: typer.Context, user_id: str | None = typer.Option(None, "--user-id")) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.list_alerts(user_id=user_id)))


@app.command("get-alert")
def get_alert(ctx: typer.Context, alert_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.get_alert(alert_id)))


@app.command("delete-alert-subscription")
def delete_alert_subscription(ctx: typer.Context, alert_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.delete_alert_subscription(alert_id)))
