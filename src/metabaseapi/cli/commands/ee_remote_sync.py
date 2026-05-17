from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object_or_empty
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.ee_remote_sync import GetEeRemoteSyncBranchesRequest
from metabaseapi.endpoints.requests.ee_remote_sync import GetEeRemoteSyncCurrentTaskRequest
from metabaseapi.endpoints.requests.ee_remote_sync import GetEeRemoteSyncDirtyRequest
from metabaseapi.endpoints.requests.ee_remote_sync import GetEeRemoteSyncHasRemoteChangesRequest
from metabaseapi.endpoints.requests.ee_remote_sync import GetEeRemoteSyncIsDirtyRequest
from metabaseapi.endpoints.requests.ee_remote_sync import PostEeRemoteSyncCreateBranchRequest
from metabaseapi.endpoints.requests.ee_remote_sync import PostEeRemoteSyncCurrentTaskCancelRequest
from metabaseapi.endpoints.requests.ee_remote_sync import PostEeRemoteSyncExportRequest
from metabaseapi.endpoints.requests.ee_remote_sync import PostEeRemoteSyncImportRequest
from metabaseapi.endpoints.requests.ee_remote_sync import PostEeRemoteSyncStashRequest
from metabaseapi.endpoints.requests.ee_remote_sync import PutEeRemoteSyncSettingsRequest


@app.command("get-api-ee-remote-sync-branches")
def get_api_ee_remote_sync_branches(ctx: typer.Context) -> None:
    """Get branches from the configured Remote Sync source."""

    run_endpoint_command(ctx, GetEeRemoteSyncBranchesRequest())


@app.command("post-api-ee-remote-sync-create-branch")
def post_api_ee_remote_sync_create_branch(
    ctx: typer.Context,
    body: str | None = typer.Argument(None, help="Optional branch creation JSON object"),
) -> None:
    """Create a new Remote Sync branch and switch to it."""

    run_endpoint_command(
        ctx,
        PostEeRemoteSyncCreateBranchRequest(body=parse_optional_json_object_or_empty(body, "body")),
    )


@app.command("get-api-ee-remote-sync-current-task")
def get_api_ee_remote_sync_current_task(ctx: typer.Context) -> None:
    """Get the current Remote Sync task."""

    run_endpoint_command(ctx, GetEeRemoteSyncCurrentTaskRequest())


@app.command("post-api-ee-remote-sync-current-task-cancel")
def post_api_ee_remote_sync_current_task_cancel(ctx: typer.Context) -> None:
    """Cancel the current Remote Sync task."""

    run_endpoint_command(ctx, PostEeRemoteSyncCurrentTaskCancelRequest())


@app.command("get-api-ee-remote-sync-dirty")
def get_api_ee_remote_sync_dirty(ctx: typer.Context) -> None:
    """Return Remote Sync models with local changes."""

    run_endpoint_command(ctx, GetEeRemoteSyncDirtyRequest())


@app.command("post-api-ee-remote-sync-export")
def post_api_ee_remote_sync_export(
    ctx: typer.Context,
    body: str | None = typer.Argument(None, help="Optional Remote Sync export JSON object"),
) -> None:
    """Export Remote Sync collection state to the configured source."""

    run_endpoint_command(ctx, PostEeRemoteSyncExportRequest(body=parse_optional_json_object_or_empty(body, "body")))


@app.command("get-api-ee-remote-sync-has-remote-changes")
def get_api_ee_remote_sync_has_remote_changes(ctx: typer.Context) -> None:
    """Check whether the remote branch has changes to pull."""

    run_endpoint_command(ctx, GetEeRemoteSyncHasRemoteChangesRequest())


@app.command("post-api-ee-remote-sync-import")
def post_api_ee_remote_sync_import(
    ctx: typer.Context,
    body: str | None = typer.Argument(None, help="Optional Remote Sync import JSON object"),
) -> None:
    """Import content from the configured Remote Sync source."""

    run_endpoint_command(ctx, PostEeRemoteSyncImportRequest(body=parse_optional_json_object_or_empty(body, "body")))


@app.command("get-api-ee-remote-sync-is-dirty")
def get_api_ee_remote_sync_is_dirty(ctx: typer.Context) -> None:
    """Check whether Remote Sync content has local changes."""

    run_endpoint_command(ctx, GetEeRemoteSyncIsDirtyRequest())


@app.command("put-api-ee-remote-sync-settings")
def put_api_ee_remote_sync_settings(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Remote Sync settings JSON object"),
) -> None:
    """Update Remote Sync settings."""

    run_json_body_endpoint_command(ctx, body, lambda payload: PutEeRemoteSyncSettingsRequest(body=payload))


@app.command("post-api-ee-remote-sync-stash")
def post_api_ee_remote_sync_stash(
    ctx: typer.Context,
    body: str | None = typer.Argument(None, help="Optional Remote Sync stash JSON object"),
) -> None:
    """Stash Remote Sync changes to a new branch."""

    run_endpoint_command(ctx, PostEeRemoteSyncStashRequest(body=parse_optional_json_object_or_empty(body, "body")))
