from __future__ import annotations

from typing import Annotated

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.revision import GetEntityRevisionsRequest
from metabaseapi.endpoints.requests.revision import GetRevisionsRequest
from metabaseapi.endpoints.requests.revision import RevertRevisionRequest
from metabaseapi.endpoints.requests.revision import RevisionEntity


@app.command("get-revisions")
def get_revisions(
    ctx: typer.Context,
    entity: Annotated[RevisionEntity, typer.Argument()],
    id: str = typer.Argument(...),
) -> None:
    """Get revisions for a card or dashboard."""

    run_endpoint_command(ctx, GetRevisionsRequest(entity=entity, id=id))


@app.command("revert-revision")
def revert_revision(
    ctx: typer.Context,
    entity: Annotated[RevisionEntity, typer.Argument()],
    id: str = typer.Argument(...),
    revision_id: str = typer.Argument(...),
) -> None:
    """Revert a card or dashboard to a prior revision."""

    run_endpoint_command(ctx, RevertRevisionRequest(entity=entity, id=id, revision_id=revision_id))


@app.command("get-entity-revisions")
def get_entity_revisions(
    ctx: typer.Context,
    entity: str = typer.Argument(...),
    id: str = typer.Argument(...),
) -> None:
    """Fetch revisions for an object by entity path."""

    run_endpoint_command(ctx, GetEntityRevisionsRequest(entity=entity, id=id))
