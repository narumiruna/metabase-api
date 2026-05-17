from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.ee_tenant import GetEeTenantIdRequest
from metabaseapi.endpoints.requests.ee_tenant import GetEeTenantRequest
from metabaseapi.endpoints.requests.ee_tenant import PostEeTenantRequest
from metabaseapi.endpoints.requests.ee_tenant import PutEeTenantIdRequest


@app.command("post-api-ee-tenant")
def post_api_ee_tenant(ctx: typer.Context, body: str = typer.Argument(..., help="Tenant JSON object")) -> None:
    """Create a tenant."""

    run_json_body_endpoint_command(ctx, body, lambda payload: PostEeTenantRequest(body=payload))


@app.command("get-api-ee-tenant")
def get_api_ee_tenant(ctx: typer.Context) -> None:
    """List tenants."""

    run_endpoint_command(ctx, GetEeTenantRequest())


@app.command("put-api-ee-tenant-id")
def put_api_ee_tenant_id(
    ctx: typer.Context,
    tenant_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Tenant update JSON object"),
) -> None:
    """Update a tenant."""

    run_json_body_endpoint_command(ctx, body, lambda payload: PutEeTenantIdRequest(tenant_id=tenant_id, body=payload))


@app.command("get-api-ee-tenant-id")
def get_api_ee_tenant_id(ctx: typer.Context, tenant_id: str = typer.Argument(...)) -> None:
    """Fetch a tenant."""

    run_endpoint_command(ctx, GetEeTenantIdRequest(tenant_id=tenant_id))
