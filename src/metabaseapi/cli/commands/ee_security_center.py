from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import parse_optional_json_object_or_empty
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.cli.runtime import run_json_body_endpoint_command
from metabaseapi.endpoints.requests.ee_security_center import AcknowledgeEeSecurityCenterAdvisoriesRequest
from metabaseapi.endpoints.requests.ee_security_center import AcknowledgeEeSecurityCenterAdvisoryRequest
from metabaseapi.endpoints.requests.ee_security_center import GetEeSecurityCenterRequest
from metabaseapi.endpoints.requests.ee_security_center import SyncEeSecurityCenterRequest
from metabaseapi.endpoints.requests.ee_security_center import TestEeSecurityCenterNotificationRequest


@app.command("get-ee-security-center")
def get_ee_security_center(ctx: typer.Context) -> None:
    """List security advisories with match status."""

    run_endpoint_command(ctx, GetEeSecurityCenterRequest())


@app.command("post-ee-security-center-acknowledge")
def post_ee_security_center_acknowledge(
    ctx: typer.Context,
    body: str = typer.Argument("{}", help="Security advisory acknowledgement JSON object"),
) -> None:
    """Acknowledge multiple security advisories."""

    run_json_body_endpoint_command(
        ctx,
        body,
        lambda payload: AcknowledgeEeSecurityCenterAdvisoriesRequest(body=payload),
    )


@app.command("post-ee-security-center-sync")
def post_ee_security_center_sync(ctx: typer.Context) -> None:
    """Trigger security advisory sync and evaluation."""

    run_endpoint_command(ctx, SyncEeSecurityCenterRequest())


@app.command("post-ee-security-center-test-notification")
def post_ee_security_center_test_notification(
    ctx: typer.Context,
    body: str | None = typer.Argument(None, help="Security Center test notification JSON object"),
) -> None:
    """Send a Security Center test notification."""

    run_endpoint_command(
        ctx,
        TestEeSecurityCenterNotificationRequest(
            body=parse_optional_json_object_or_empty(body, "body"),
        ),
    )


@app.command("post-ee-security-center-advisory-id-acknowledge")
def post_ee_security_center_advisory_id_acknowledge(
    ctx: typer.Context,
    advisory_id: str = typer.Argument(...),
    body: str | None = typer.Argument(None, help="Security advisory acknowledgement JSON object"),
) -> None:
    """Acknowledge one security advisory."""

    run_endpoint_command(
        ctx,
        AcknowledgeEeSecurityCenterAdvisoryRequest(
            advisory_id=advisory_id,
            body=parse_optional_json_object_or_empty(body, "body"),
        ),
    )
