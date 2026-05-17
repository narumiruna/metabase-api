from __future__ import annotations

import typer

from metabaseapi.cli.runtime import _run_and_print
from metabaseapi.cli.runtime import _run_client_call
from metabaseapi.cli.runtime import app
from metabaseapi.client.raw import bug_reporting as _raw_bug_reporting


@app.command("bug-reporting-connection-pool-details")
def bug_reporting_connection_pool_details(ctx: typer.Context) -> None:
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: _raw_bug_reporting.bug_reporting_connection_pool_details(
                client,
            ),
        )
    )


@app.command("bug-reporting-details")
def bug_reporting_details(ctx: typer.Context) -> None:
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: _raw_bug_reporting.bug_reporting_details(
                client,
            ),
        )
    )
