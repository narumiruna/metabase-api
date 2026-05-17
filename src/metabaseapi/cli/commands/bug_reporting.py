from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.bug_reporting import GetBugReportingConnectionPoolDetailsRequest
from metabaseapi.endpoints.requests.bug_reporting import GetBugReportingDetailsRequest


@app.command("bug-reporting-connection-pool-details")
def bug_reporting_connection_pool_details(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, GetBugReportingConnectionPoolDetailsRequest())


@app.command("bug-reporting-details")
def bug_reporting_details(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, GetBugReportingDetailsRequest())
