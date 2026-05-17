from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.ee_audit_app import DeleteEeAuditAppUserSubscriptionsRequest
from metabaseapi.endpoints.requests.ee_audit_app import GetEeAuditAppUserAuditInfoRequest
from metabaseapi.endpoints.requests.ee_audit_app import PostEeAuditAppAnalyticsDevExportRequest


@app.command("post-ee-audit-app-analytics-dev-export")
def post_ee_audit_app_analytics_dev_export(ctx: typer.Context) -> None:
    """Export audit analytics content for local development."""

    run_endpoint_command(ctx, PostEeAuditAppAnalyticsDevExportRequest())


@app.command("get-ee-audit-app-user-audit-info")
def get_ee_audit_app_user_audit_info(ctx: typer.Context) -> None:
    """Fetch audit app information for the current user."""

    run_endpoint_command(ctx, GetEeAuditAppUserAuditInfoRequest())


@app.command("delete-ee-audit-app-user-id-subscriptions")
def delete_ee_audit_app_user_id_subscriptions(ctx: typer.Context, id: str = typer.Argument(...)) -> None:
    """Delete all audit-related subscriptions for a user."""

    run_endpoint_command(ctx, DeleteEeAuditAppUserSubscriptionsRequest(id=id))
