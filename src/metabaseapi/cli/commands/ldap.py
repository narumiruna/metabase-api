from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.ldap import UpdateLdapSettingsRequest


@app.command("put-api-ldap-settings")
def put_api_ldap_settings(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="LDAP settings JSON object"),
) -> None:
    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateLdapSettingsRequest(body=payload))
