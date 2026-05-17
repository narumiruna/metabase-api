from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.ee_billing import GetEeBillingRequest


@app.command("get-ee-billing")
def get_ee_billing(ctx: typer.Context) -> None:
    """Fetch EE billing information."""

    run_endpoint_command(ctx, GetEeBillingRequest())
