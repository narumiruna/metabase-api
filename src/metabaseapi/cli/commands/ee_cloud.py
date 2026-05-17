from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.ee_cloud import DeleteEeCloudAddOnsProductTypeRequest
from metabaseapi.endpoints.requests.ee_cloud import GetEeCloudAddOnsAddonsRequest
from metabaseapi.endpoints.requests.ee_cloud import GetEeCloudAddOnsPlansRequest
from metabaseapi.endpoints.requests.ee_cloud import PostEeCloudAddOnsProductTypeRequest
from metabaseapi.endpoints.requests.ee_cloud import PostEeCloudProxyOperationIdRequest


@app.command("get-ee-cloud-add-ons-addons")
def get_ee_cloud_add_ons_addons(ctx: typer.Context) -> None:
    """Fetch cloud add-ons information."""

    run_endpoint_command(ctx, GetEeCloudAddOnsAddonsRequest())


@app.command("get-ee-cloud-add-ons-plans")
def get_ee_cloud_add_ons_plans(ctx: typer.Context) -> None:
    """Fetch cloud add-on plans information."""

    run_endpoint_command(ctx, GetEeCloudAddOnsPlansRequest())


@app.command("post-ee-cloud-add-ons-product-type")
def post_ee_cloud_add_ons_product_type(
    ctx: typer.Context,
    product_type: str = typer.Argument(...),
    body: str = typer.Argument("{}", help="Cloud add-on purchase JSON object"),
) -> None:
    """Purchase a cloud add-on."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: PostEeCloudAddOnsProductTypeRequest(product_type=product_type, body=payload),
    )


@app.command("delete-ee-cloud-add-ons-product-type")
def delete_ee_cloud_add_ons_product_type(ctx: typer.Context, product_type: str = typer.Argument(...)) -> None:
    """Remove a cloud add-on."""

    run_endpoint_command(ctx, DeleteEeCloudAddOnsProductTypeRequest(product_type=product_type))


@app.command("post-ee-cloud-proxy-operation-id")
def post_ee_cloud_proxy_operation_id(
    ctx: typer.Context,
    operation_id: str = typer.Argument(...),
    body: str = typer.Argument("{}", help="Cloud proxy operation JSON object"),
) -> None:
    """Proxy a hosted cloud operation."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: PostEeCloudProxyOperationIdRequest(operation_id=operation_id, body=payload),
    )
