from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.login_history import GetCurrentLoginHistoryRequest


@app.command("get-login-history-current")
def get_login_history_current(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, GetCurrentLoginHistoryRequest())
