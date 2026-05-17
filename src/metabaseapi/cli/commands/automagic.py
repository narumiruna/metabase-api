from __future__ import annotations

import typer

from metabaseapi.cli.runtime import _run_and_print
from metabaseapi.cli.runtime import _run_client_call
from metabaseapi.cli.runtime import app


@app.command("automagic-database-candidates")
def automagic_database_candidates(ctx: typer.Context, database_id: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.automagic_database_candidates(database_id)))


@app.command("automagic-model-index-primary-key")
def automagic_model_index_primary_key(
    ctx: typer.Context,
    model_index_id: str = typer.Argument(...),
    primary_key_id: str = typer.Argument(...),
) -> None:
    _run_and_print(
        _run_client_call(ctx, lambda client: client.automagic_model_index_primary_key(model_index_id, primary_key_id)),
    )


@app.command("automagic-dashboard-path")
def automagic_dashboard_path(ctx: typer.Context, path: str = typer.Argument(...)) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.automagic_dashboard_path(path)))


@app.command("automagic-entity")
def automagic_entity(ctx: typer.Context, entity: str, entity_id_or_query: str) -> None:
    _run_and_print(_run_client_call(ctx, lambda client: client.automagic_entity(entity, entity_id_or_query)))


@app.command("automagic-entity-cell")
def automagic_entity_cell(ctx: typer.Context, entity: str, entity_id_or_query: str, cell_query: str) -> None:
    _run_and_print(
        _run_client_call(ctx, lambda client: client.automagic_entity_cell(entity, entity_id_or_query, cell_query))
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
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.automagic_entity_cell_compare(
                entity,
                entity_id_or_query,
                cell_query,
                comparison_entity,
                comparison_entity_id_or_query,
            ),
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
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.automagic_entity_cell_rule(
                entity, entity_id_or_query, cell_query, prefix, dashboard_template
            ),
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
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.automagic_entity_cell_rule_compare(
                entity,
                entity_id_or_query,
                cell_query,
                prefix,
                dashboard_template,
                comparison_entity,
                comparison_entity_id_or_query,
            ),
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
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.automagic_entity_compare(
                entity,
                entity_id_or_query,
                comparison_entity,
                comparison_entity_id_or_query,
            ),
        ),
    )


@app.command("automagic-entity-query-metadata")
def automagic_entity_query_metadata(ctx: typer.Context, entity: str, entity_id_or_query: str) -> None:
    _run_and_print(
        _run_client_call(ctx, lambda client: client.automagic_entity_query_metadata(entity, entity_id_or_query))
    )


@app.command("automagic-entity-rule")
def automagic_entity_rule(
    ctx: typer.Context,
    entity: str,
    entity_id_or_query: str,
    prefix: str,
    dashboard_template: str,
) -> None:
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.automagic_entity_rule(entity, entity_id_or_query, prefix, dashboard_template),
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
    _run_and_print(
        _run_client_call(
            ctx,
            lambda client: client.automagic_entity_rule_compare(
                entity,
                entity_id_or_query,
                prefix,
                dashboard_template,
                comparison_entity,
                comparison_entity_id_or_query,
            ),
        ),
    )
