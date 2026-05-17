from __future__ import annotations

import typer

from metabaseapi.cli.runtime import app
from metabaseapi.cli.runtime import run_endpoint_command
from metabaseapi.endpoints.requests.automagic import AutomagicDashboardRequest
from metabaseapi.endpoints.requests.automagic import AutomagicDatabaseCandidatesRequest
from metabaseapi.endpoints.requests.automagic import AutomagicEntityCellCompareRequest
from metabaseapi.endpoints.requests.automagic import AutomagicEntityCellRequest
from metabaseapi.endpoints.requests.automagic import AutomagicEntityCellRuleCompareRequest
from metabaseapi.endpoints.requests.automagic import AutomagicEntityCellRuleRequest
from metabaseapi.endpoints.requests.automagic import AutomagicEntityCompareRequest
from metabaseapi.endpoints.requests.automagic import AutomagicEntityQueryMetadataRequest
from metabaseapi.endpoints.requests.automagic import AutomagicEntityRequest
from metabaseapi.endpoints.requests.automagic import AutomagicEntityRuleCompareRequest
from metabaseapi.endpoints.requests.automagic import AutomagicEntityRuleRequest
from metabaseapi.endpoints.requests.automagic import AutomagicModelIndexPrimaryKeyRequest


def _run_automagic_path(ctx: typer.Context, path: str) -> None:
    run_endpoint_command(ctx, AutomagicDashboardRequest(path=path))


@app.command("automagic-database-candidates")
def automagic_database_candidates(ctx: typer.Context, database_id: str = typer.Argument(...)) -> None:
    run_endpoint_command(ctx, AutomagicDatabaseCandidatesRequest(database_id=database_id))


@app.command("automagic-model-index-primary-key")
def automagic_model_index_primary_key(
    ctx: typer.Context,
    model_index_id: str = typer.Argument(...),
    primary_key_id: str = typer.Argument(...),
) -> None:
    run_endpoint_command(
        ctx, AutomagicModelIndexPrimaryKeyRequest(model_index_id=model_index_id, primary_key_id=primary_key_id)
    )


@app.command("automagic-dashboard-path")
def automagic_dashboard_path(ctx: typer.Context, path: str = typer.Argument(...)) -> None:
    _run_automagic_path(ctx, path)


@app.command("automagic-entity")
def automagic_entity(ctx: typer.Context, entity: str, entity_id_or_query: str) -> None:
    run_endpoint_command(ctx, AutomagicEntityRequest(entity=entity, entity_id_or_query=entity_id_or_query))


@app.command("automagic-entity-cell")
def automagic_entity_cell(ctx: typer.Context, entity: str, entity_id_or_query: str, cell_query: str) -> None:
    run_endpoint_command(
        ctx,
        AutomagicEntityCellRequest(entity=entity, entity_id_or_query=entity_id_or_query, cell_query=cell_query),
    )


@app.command("automagic-entity-cell-compare")
def automagic_entity_cell_compare(
    ctx: typer.Context,
    entity: str,
    entity_id_or_query: str,
    cell_query: str,
    comparison_entity: str,
    comparison_entity_id_or_query: str,
) -> None:
    run_endpoint_command(
        ctx,
        AutomagicEntityCellCompareRequest(
            entity=entity,
            entity_id_or_query=entity_id_or_query,
            cell_query=cell_query,
            comparison_entity=comparison_entity,
            comparison_entity_id_or_query=comparison_entity_id_or_query,
        ),
    )


@app.command("automagic-entity-cell-rule")
def automagic_entity_cell_rule(
    ctx: typer.Context,
    entity: str,
    entity_id_or_query: str,
    cell_query: str,
    prefix: str,
    dashboard_template: str,
) -> None:
    run_endpoint_command(
        ctx,
        AutomagicEntityCellRuleRequest(
            entity=entity,
            entity_id_or_query=entity_id_or_query,
            cell_query=cell_query,
            prefix=prefix,
            dashboard_template=dashboard_template,
        ),
    )


@app.command("automagic-entity-cell-rule-compare")
def automagic_entity_cell_rule_compare(
    ctx: typer.Context,
    entity: str,
    entity_id_or_query: str,
    cell_query: str,
    prefix: str,
    dashboard_template: str,
    comparison_entity: str,
    comparison_entity_id_or_query: str,
) -> None:
    run_endpoint_command(
        ctx,
        AutomagicEntityCellRuleCompareRequest(
            entity=entity,
            entity_id_or_query=entity_id_or_query,
            cell_query=cell_query,
            prefix=prefix,
            dashboard_template=dashboard_template,
            comparison_entity=comparison_entity,
            comparison_entity_id_or_query=comparison_entity_id_or_query,
        ),
    )


@app.command("automagic-entity-compare")
def automagic_entity_compare(
    ctx: typer.Context,
    entity: str,
    entity_id_or_query: str,
    comparison_entity: str,
    comparison_entity_id_or_query: str,
) -> None:
    run_endpoint_command(
        ctx,
        AutomagicEntityCompareRequest(
            entity=entity,
            entity_id_or_query=entity_id_or_query,
            comparison_entity=comparison_entity,
            comparison_entity_id_or_query=comparison_entity_id_or_query,
        ),
    )


@app.command("automagic-entity-query-metadata")
def automagic_entity_query_metadata(ctx: typer.Context, entity: str, entity_id_or_query: str) -> None:
    run_endpoint_command(ctx, AutomagicEntityQueryMetadataRequest(entity=entity, entity_id_or_query=entity_id_or_query))


@app.command("automagic-entity-rule")
def automagic_entity_rule(
    ctx: typer.Context,
    entity: str,
    entity_id_or_query: str,
    prefix: str,
    dashboard_template: str,
) -> None:
    run_endpoint_command(
        ctx,
        AutomagicEntityRuleRequest(
            entity=entity,
            entity_id_or_query=entity_id_or_query,
            prefix=prefix,
            dashboard_template=dashboard_template,
        ),
    )


@app.command("automagic-entity-rule-compare")
def automagic_entity_rule_compare(
    ctx: typer.Context,
    entity: str,
    entity_id_or_query: str,
    prefix: str,
    dashboard_template: str,
    comparison_entity: str,
    comparison_entity_id_or_query: str,
) -> None:
    run_endpoint_command(
        ctx,
        AutomagicEntityRuleCompareRequest(
            entity=entity,
            entity_id_or_query=entity_id_or_query,
            prefix=prefix,
            dashboard_template=dashboard_template,
            comparison_entity=comparison_entity,
            comparison_entity_id_or_query=comparison_entity_id_or_query,
        ),
    )
