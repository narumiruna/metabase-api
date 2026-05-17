from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.ee_ai_controls import DisableEeAiControlsAdvancedPermissionsRequest
from metabaseapi.endpoints.requests.ee_ai_controls import EnableEeAiControlsAdvancedPermissionsRequest
from metabaseapi.endpoints.requests.ee_ai_controls import GetEeAiControlsPermissionsRequest
from metabaseapi.endpoints.requests.ee_ai_controls import GetEeAiControlsUsageGroupIdRequest
from metabaseapi.endpoints.requests.ee_ai_controls import GetEeAiControlsUsageGroupRequest
from metabaseapi.endpoints.requests.ee_ai_controls import GetEeAiControlsUsageInstanceRequest
from metabaseapi.endpoints.requests.ee_ai_controls import GetEeAiControlsUsageTenantIdRequest
from metabaseapi.endpoints.requests.ee_ai_controls import GetEeAiControlsUsageTenantRequest
from metabaseapi.endpoints.requests.ee_ai_controls import PutEeAiControlsPermissionsRequest
from metabaseapi.endpoints.requests.ee_ai_controls import PutEeAiControlsUsageGroupIdRequest
from metabaseapi.endpoints.requests.ee_ai_controls import PutEeAiControlsUsageInstanceRequest
from metabaseapi.endpoints.requests.ee_ai_controls import PutEeAiControlsUsageTenantIdRequest


@app.command("get-ee-ai-controls-permissions")
def get_ee_ai_controls_permissions(ctx: typer.Context) -> None:
    """Fetch EE AI controls permissions."""

    run_endpoint_command(ctx, GetEeAiControlsPermissionsRequest())


@app.command("put-ee-ai-controls-permissions")
def put_ee_ai_controls_permissions(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="AI controls permissions JSON object"),
) -> None:
    """Update EE AI controls permissions."""

    run_json_body_endpoint_command(ctx, body, lambda payload: PutEeAiControlsPermissionsRequest(body=payload))


@app.command("enable-ee-ai-controls-permissions-advanced")
def enable_ee_ai_controls_permissions_advanced(ctx: typer.Context) -> None:
    """Switch EE AI controls permissions to advanced mode."""

    run_endpoint_command(ctx, EnableEeAiControlsAdvancedPermissionsRequest())


@app.command("disable-ee-ai-controls-permissions-advanced")
def disable_ee_ai_controls_permissions_advanced(ctx: typer.Context) -> None:
    """Switch EE AI controls permissions to simple mode."""

    run_endpoint_command(ctx, DisableEeAiControlsAdvancedPermissionsRequest())


@app.command("get-ee-ai-controls-usage-instance")
def get_ee_ai_controls_usage_instance(ctx: typer.Context) -> None:
    """Fetch the EE AI controls instance usage limit."""

    run_endpoint_command(ctx, GetEeAiControlsUsageInstanceRequest())


@app.command("put-ee-ai-controls-usage-instance")
def put_ee_ai_controls_usage_instance(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Instance usage limit JSON object"),
) -> None:
    """Set the EE AI controls instance usage limit."""

    run_json_body_endpoint_command(ctx, body, lambda payload: PutEeAiControlsUsageInstanceRequest(body=payload))


@app.command("get-ee-ai-controls-usage-tenant")
def get_ee_ai_controls_usage_tenant(ctx: typer.Context) -> None:
    """Fetch all EE AI controls tenant usage limits."""

    run_endpoint_command(ctx, GetEeAiControlsUsageTenantRequest())


@app.command("get-ee-ai-controls-usage-tenant-id")
def get_ee_ai_controls_usage_tenant_id(ctx: typer.Context, tenant_id: str = typer.Argument(...)) -> None:
    """Fetch an EE AI controls tenant usage limit."""

    run_endpoint_command(ctx, GetEeAiControlsUsageTenantIdRequest(tenant_id=tenant_id))


@app.command("put-ee-ai-controls-usage-tenant-id")
def put_ee_ai_controls_usage_tenant_id(
    ctx: typer.Context,
    tenant_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Tenant usage limit JSON object"),
) -> None:
    """Set an EE AI controls tenant usage limit."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: PutEeAiControlsUsageTenantIdRequest(tenant_id=tenant_id, body=payload),
    )


@app.command("get-ee-ai-controls-usage-group")
def get_ee_ai_controls_usage_group(ctx: typer.Context) -> None:
    """Fetch all EE AI controls group usage limits."""

    run_endpoint_command(ctx, GetEeAiControlsUsageGroupRequest())


@app.command("get-ee-ai-controls-usage-group-id")
def get_ee_ai_controls_usage_group_id(ctx: typer.Context, group_id: str = typer.Argument(...)) -> None:
    """Fetch an EE AI controls group usage limit."""

    run_endpoint_command(ctx, GetEeAiControlsUsageGroupIdRequest(group_id=group_id))


@app.command("put-ee-ai-controls-usage-group-id")
def put_ee_ai_controls_usage_group_id(
    ctx: typer.Context,
    group_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Group usage limit JSON object"),
) -> None:
    """Set an EE AI controls group usage limit."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: PutEeAiControlsUsageGroupIdRequest(group_id=group_id, body=payload),
    )
