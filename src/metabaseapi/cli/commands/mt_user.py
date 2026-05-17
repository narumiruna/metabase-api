from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.mt_user import GetMtUserAttributesRequest
from metabaseapi.endpoints.requests.mt_user import PutMtUserIdAttributesRequest


@app.command("get-api-mt-user-attributes")
def get_api_mt_user_attributes(ctx: typer.Context) -> None:
    """List possible user login attribute keys."""

    run_endpoint_command(ctx, GetMtUserAttributesRequest())


@app.command("put-api-mt-user-id-attributes")
def put_api_mt_user_id_attributes(
    ctx: typer.Context,
    user_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="User login attributes JSON object"),
) -> None:
    """Update user login attributes."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: PutMtUserIdAttributesRequest(user_id=user_id, body=payload),
    )
