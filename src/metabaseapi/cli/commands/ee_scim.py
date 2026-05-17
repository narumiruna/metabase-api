from __future__ import annotations

from typing import Annotated

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.ee_scim import CreateEeScimApiKeyRequest
from metabaseapi.endpoints.requests.ee_scim import CreateEeScimV2GroupRequest
from metabaseapi.endpoints.requests.ee_scim import CreateEeScimV2UserRequest
from metabaseapi.endpoints.requests.ee_scim import DeleteEeScimV2GroupRequest
from metabaseapi.endpoints.requests.ee_scim import GetEeScimApiKeyRequest
from metabaseapi.endpoints.requests.ee_scim import GetEeScimV2GroupRequest
from metabaseapi.endpoints.requests.ee_scim import GetEeScimV2UserRequest
from metabaseapi.endpoints.requests.ee_scim import ListEeScimV2GroupsRequest
from metabaseapi.endpoints.requests.ee_scim import ListEeScimV2UsersRequest
from metabaseapi.endpoints.requests.ee_scim import PatchEeScimV2UserRequest
from metabaseapi.endpoints.requests.ee_scim import UpdateEeScimV2GroupRequest
from metabaseapi.endpoints.requests.ee_scim import UpdateEeScimV2UserRequest


@app.command("get-ee-scim-api-key")
def get_ee_scim_api_key(ctx: typer.Context) -> None:
    """Fetch the SCIM API key metadata."""

    run_endpoint_command(ctx, GetEeScimApiKeyRequest())


@app.command("post-ee-scim-api-key")
def post_ee_scim_api_key(ctx: typer.Context) -> None:
    """Create or refresh the SCIM API key."""

    run_endpoint_command(ctx, CreateEeScimApiKeyRequest())


@app.command("get-ee-scim-v2-groups")
def get_ee_scim_v2_groups(
    ctx: typer.Context,
    filter: Annotated[str | None, typer.Option("--filter")] = None,
    start_index: Annotated[int | None, typer.Option("--start-index")] = None,
    count: Annotated[int | None, typer.Option("--count")] = None,
) -> None:
    """Fetch SCIM groups."""

    run_endpoint_command(ctx, ListEeScimV2GroupsRequest(filter=filter, start_index=start_index, count=count))


@app.command("post-ee-scim-v2-groups")
def post_ee_scim_v2_groups(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="SCIM group JSON object"),
) -> None:
    """Create a SCIM group."""

    run_json_body_endpoint_command(ctx, body, lambda payload: CreateEeScimV2GroupRequest(body=payload))


@app.command("get-ee-scim-v2-groups-id")
def get_ee_scim_v2_groups_id(ctx: typer.Context, group_id: str = typer.Argument(...)) -> None:
    """Fetch a SCIM group."""

    run_endpoint_command(ctx, GetEeScimV2GroupRequest(group_id=group_id))


@app.command("put-ee-scim-v2-groups-id")
def put_ee_scim_v2_groups_id(
    ctx: typer.Context,
    group_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="SCIM group JSON object"),
) -> None:
    """Update a SCIM group."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: UpdateEeScimV2GroupRequest(group_id=group_id, body=payload),
    )


@app.command("delete-ee-scim-v2-groups-id")
def delete_ee_scim_v2_groups_id(ctx: typer.Context, group_id: str = typer.Argument(...)) -> None:
    """Delete a SCIM group."""

    run_endpoint_command(ctx, DeleteEeScimV2GroupRequest(group_id=group_id))


@app.command("get-ee-scim-v2-users")
def get_ee_scim_v2_users(
    ctx: typer.Context,
    filter: Annotated[str | None, typer.Option("--filter")] = None,
    start_index: Annotated[int | None, typer.Option("--start-index")] = None,
    count: Annotated[int | None, typer.Option("--count")] = None,
) -> None:
    """Fetch SCIM users."""

    run_endpoint_command(ctx, ListEeScimV2UsersRequest(filter=filter, start_index=start_index, count=count))


@app.command("post-ee-scim-v2-users")
def post_ee_scim_v2_users(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="SCIM user JSON object"),
) -> None:
    """Create a SCIM user."""

    run_json_body_endpoint_command(ctx, body, lambda payload: CreateEeScimV2UserRequest(body=payload))


@app.command("get-ee-scim-v2-users-id")
def get_ee_scim_v2_users_id(ctx: typer.Context, user_id: str = typer.Argument(...)) -> None:
    """Fetch a SCIM user."""

    run_endpoint_command(ctx, GetEeScimV2UserRequest(user_id=user_id))


@app.command("put-ee-scim-v2-users-id")
def put_ee_scim_v2_users_id(
    ctx: typer.Context,
    user_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="SCIM user JSON object"),
) -> None:
    """Update a SCIM user."""

    run_json_body_endpoint_command(ctx, body, lambda payload: UpdateEeScimV2UserRequest(user_id=user_id, body=payload))


@app.command("patch-ee-scim-v2-users-id")
def patch_ee_scim_v2_users_id(
    ctx: typer.Context,
    user_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="SCIM user patch JSON object"),
) -> None:
    """Activate or deactivate a SCIM user."""

    run_json_body_endpoint_command(ctx, body, lambda payload: PatchEeScimV2UserRequest(user_id=user_id, body=payload))
