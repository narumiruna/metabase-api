from __future__ import annotations

import typer

from metabaseapi.cli.runtime import _run_and_print
from metabaseapi.cli.runtime import _run_client_call
from metabaseapi.cli.runtime import app


@app.command("bug-reporting-connection-pool-details")
def bug_reporting_connection_pool_details(ctx: typer.Context) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.bug_reporting_connection_pool_details()))


@app.command("bug-reporting-details")
def bug_reporting_details(ctx: typer.Context) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.bug_reporting_details()))
