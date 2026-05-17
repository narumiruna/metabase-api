from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.ee_database_routing import PostEeDatabaseRoutingDestinationDatabaseRequest
from metabaseapi.endpoints.requests.ee_database_routing import PutEeDatabaseRoutingRouterDatabaseIdRequest


@app.command("post-ee-database-routing-destination-database")
def post_ee_database_routing_destination_database(
    ctx: typer.Context,
    body: str = typer.Argument(..., help="Destination database JSON object"),
) -> None:
    """Create an EE database routing destination database."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: PostEeDatabaseRoutingDestinationDatabaseRequest(body=payload),
    )


@app.command("put-ee-database-routing-router-database-id")
def put_ee_database_routing_router_database_id(
    ctx: typer.Context,
    id: str = typer.Argument(...),
    body: str = typer.Argument(..., help="Router database JSON object"),
) -> None:
    """Update an EE database routing router database."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: PutEeDatabaseRoutingRouterDatabaseIdRequest(id=id, body=payload),
    )
