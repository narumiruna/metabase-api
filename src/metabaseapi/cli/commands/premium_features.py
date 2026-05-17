from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.premium_features import GetPremiumFeaturesTokenStatusRequest
from metabaseapi.endpoints.requests.premium_features import RefreshPremiumFeaturesTokenRequest


@app.command("post-api-premium-features-token-refresh")
def post_api_premium_features_token_refresh(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, RefreshPremiumFeaturesTokenRequest())


@app.command("get-api-premium-features-token-status")
def get_api_premium_features_token_status(ctx: typer.Context) -> None:
    run_endpoint_command(ctx, GetPremiumFeaturesTokenStatusRequest())
