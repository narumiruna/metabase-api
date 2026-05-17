from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.ee_database_replication import (
    DeleteEeDatabaseReplicationConnectionDatabaseIdRequest,
)
from metabaseapi.endpoints.requests.ee_database_replication import (
    PostEeDatabaseReplicationConnectionDatabaseIdPreviewRequest,
)
from metabaseapi.endpoints.requests.ee_database_replication import PostEeDatabaseReplicationConnectionDatabaseIdRequest


@app.command("post-ee-database-replication-connection-database-id")
def post_ee_database_replication_connection_database_id(
    ctx: typer.Context,
    database_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Database replication connection JSON object"),
) -> None:
    """Create a PG replication connection for a database."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: PostEeDatabaseReplicationConnectionDatabaseIdRequest(database_id=database_id, body=payload),
    )


@app.command("delete-ee-database-replication-connection-database-id")
def delete_ee_database_replication_connection_database_id(
    ctx: typer.Context,
    database_id: str = typer.Argument(...),
) -> None:
    """Delete a PG replication connection for a database."""

    run_endpoint_command(ctx, DeleteEeDatabaseReplicationConnectionDatabaseIdRequest(database_id=database_id))


@app.command("post-ee-database-replication-connection-database-id-preview")
def post_ee_database_replication_connection_database_id_preview(
    ctx: typer.Context,
    database_id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Database replication preview JSON object"),
) -> None:
    """Preview a PG replication connection for a database."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: PostEeDatabaseReplicationConnectionDatabaseIdPreviewRequest(
            database_id=database_id,
            body=payload,
        ),
    )
