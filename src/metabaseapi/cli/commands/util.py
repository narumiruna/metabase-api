from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.util import GetRandomTokenRequest


@app.command("get-random-token")
def get_random_token(ctx: typer.Context) -> None:
    """Generate a random embedding secret token."""

    run_endpoint_command(ctx, GetRandomTokenRequest())
