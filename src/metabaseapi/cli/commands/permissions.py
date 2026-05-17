from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.permissions import ClearPermissionsMembershipRequest
from metabaseapi.endpoints.requests.permissions import CreatePermissionsGroupRequest
from metabaseapi.endpoints.requests.permissions import CreatePermissionsMembershipRequest
from metabaseapi.endpoints.requests.permissions import DeletePermissionsGroupRequest
from metabaseapi.endpoints.requests.permissions import DeletePermissionsMembershipRequest
from metabaseapi.endpoints.requests.permissions import GetPermissionsGraphDbRequest
from metabaseapi.endpoints.requests.permissions import GetPermissionsGraphGroupRequest
from metabaseapi.endpoints.requests.permissions import GetPermissionsGraphRequest
from metabaseapi.endpoints.requests.permissions import GetPermissionsGroupRequest
from metabaseapi.endpoints.requests.permissions import GetPermissionsMembershipRequest
from metabaseapi.endpoints.requests.permissions import ListPermissionsGroupsRequest
from metabaseapi.endpoints.requests.permissions import PutPermissionsGraphRequest
from metabaseapi.endpoints.requests.permissions import UpdatePermissionsGroupRequest
from metabaseapi.endpoints.requests.permissions import UpdatePermissionsMembershipRequest


@app.command("get-permissions-graph")
def get_permissions_graph(ctx: typer.Context) -> None:
    """Fetch the permissions graph."""

    run_endpoint_command(ctx, GetPermissionsGraphRequest())


@app.command("put-permissions-graph")
def put_permissions_graph(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Permissions graph JSON object"),
) -> None:
    """Update permissions via graph payload."""

    run_json_body_endpoint_command(ctx, body, lambda payload: PutPermissionsGraphRequest(body=payload))


@app.command("get-permissions-graph-db")
def get_permissions_graph_db(ctx: typer.Context, db_id: str = typer.Argument(...)) -> None:
    """Fetch the permissions graph for a database."""

    run_endpoint_command(ctx, GetPermissionsGraphDbRequest(db_id=db_id))


@app.command("get-permissions-graph-group")
def get_permissions_graph_group(ctx: typer.Context, group_id: str = typer.Argument(...)) -> None:
    """Fetch the permissions graph for a group."""

    run_endpoint_command(ctx, GetPermissionsGraphGroupRequest(group_id=group_id))


@app.command("list-permissions-groups")
def list_permissions_groups(ctx: typer.Context) -> None:
    """List permissions groups."""

    run_endpoint_command(ctx, ListPermissionsGroupsRequest())


@app.command("create-permissions-group")
def create_permissions_group(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Permissions group JSON object"),
) -> None:
    """Create a permissions group."""

    run_json_body_endpoint_command(ctx, body, lambda payload: CreatePermissionsGroupRequest(body=payload))


@app.command("update-permissions-group")
def update_permissions_group(
    ctx: typer.Context,
    group_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Permissions group update JSON object"),
) -> None:
    """Update a permissions group."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: UpdatePermissionsGroupRequest(group_id=group_id, body=payload),
    )


@app.command("delete-permissions-group")
def delete_permissions_group(ctx: typer.Context, group_id: str = typer.Argument(...)) -> None:
    """Delete a permissions group."""

    run_endpoint_command(ctx, DeletePermissionsGroupRequest(group_id=group_id))


@app.command("get-permissions-group")
def get_permissions_group(ctx: typer.Context, group_id: str = typer.Argument(...)) -> None:
    """Get a permissions group."""

    run_endpoint_command(ctx, GetPermissionsGroupRequest(group_id=group_id))


@app.command("get-permissions-membership")
def get_permissions_membership(ctx: typer.Context) -> None:
    """Fetch permissions group memberships."""

    run_endpoint_command(ctx, GetPermissionsMembershipRequest())


@app.command("create-permissions-membership")
def create_permissions_membership(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Permissions membership JSON object"),
) -> None:
    """Add a user to a permissions group."""

    run_json_body_endpoint_command(ctx, body, lambda payload: CreatePermissionsMembershipRequest(body=payload))


@app.command("clear-permissions-membership")
def clear_permissions_membership(ctx: typer.Context, group_id: str = typer.Argument(...)) -> None:
    """Remove all members from a permissions group."""

    run_endpoint_command(ctx, ClearPermissionsMembershipRequest(group_id=group_id))


@app.command("update-permissions-membership")
def update_permissions_membership(
    ctx: typer.Context,
    membership_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Permissions membership update JSON object"),
) -> None:
    """Update a permissions group membership."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: UpdatePermissionsMembershipRequest(membership_id=membership_id, body=payload),
    )


@app.command("delete-permissions-membership")
def delete_permissions_membership(ctx: typer.Context, membership_id: str = typer.Argument(...)) -> None:
    """Remove a user from a permissions group."""

    run_endpoint_command(ctx, DeletePermissionsMembershipRequest(membership_id=membership_id))
