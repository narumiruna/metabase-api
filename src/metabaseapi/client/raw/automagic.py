from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.wire import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def automagic_database_candidates(client: MetabaseClient, database_id: int | str) -> JSONValue | None:
    return await client.get(f"/api/automagic-dashboards/database/{database_id}/candidates")


async def automagic_model_index_primary_key(
    client: MetabaseClient,
    model_index_id: int | str,
    primary_key_id: int | str,
) -> JSONValue | None:
    return await client.get(f"/api/automagic-dashboards/model_index/{model_index_id}/primary_key/{primary_key_id}")


async def automagic_dashboard_path(client: MetabaseClient, path: str) -> JSONValue | None:
    return await client.get(f"/api/automagic-dashboards/{path.lstrip('/')}")


async def automagic_entity(client: MetabaseClient, entity: str, entity_id_or_query: str) -> JSONValue | None:
    return await automagic_dashboard_path(client, f"{entity}/{entity_id_or_query}")


async def automagic_entity_cell(
    client: MetabaseClient,
    entity: str,
    entity_id_or_query: str,
    cell_query: str,
) -> JSONValue | None:
    return await automagic_dashboard_path(client, f"{entity}/{entity_id_or_query}/cell/{cell_query}")


async def automagic_entity_cell_compare(
    client: MetabaseClient,
    entity: str,
    entity_id_or_query: str,
    cell_query: str,
    comparison_entity: str,
    comparison_entity_id_or_query: str,
) -> JSONValue | None:
    return await automagic_dashboard_path(
        client,
        f"{entity}/{entity_id_or_query}/cell/{cell_query}/compare/{comparison_entity}/{comparison_entity_id_or_query}",
    )


async def automagic_entity_cell_rule(
    client: MetabaseClient,
    entity: str,
    entity_id_or_query: str,
    cell_query: str,
    prefix: str,
    dashboard_template: str,
) -> JSONValue | None:
    return await automagic_dashboard_path(
        client, f"{entity}/{entity_id_or_query}/cell/{cell_query}/rule/{prefix}/{dashboard_template}"
    )


async def automagic_entity_cell_rule_compare(
    client: MetabaseClient,
    entity: str,
    entity_id_or_query: str,
    cell_query: str,
    prefix: str,
    dashboard_template: str,
    comparison_entity: str,
    comparison_entity_id_or_query: str,
) -> JSONValue | None:
    return await automagic_dashboard_path(
        client,
        f"{entity}/{entity_id_or_query}/cell/{cell_query}/rule/{prefix}/{dashboard_template}/compare/{comparison_entity}/{comparison_entity_id_or_query}",
    )


async def automagic_entity_compare(
    client: MetabaseClient,
    entity: str,
    entity_id_or_query: str,
    comparison_entity: str,
    comparison_entity_id_or_query: str,
) -> JSONValue | None:
    return await automagic_dashboard_path(
        client, f"{entity}/{entity_id_or_query}/compare/{comparison_entity}/{comparison_entity_id_or_query}"
    )


async def automagic_entity_query_metadata(
    client: MetabaseClient,
    entity: str,
    entity_id_or_query: str,
) -> JSONValue | None:
    return await automagic_dashboard_path(client, f"{entity}/{entity_id_or_query}/query_metadata")


async def automagic_entity_rule(
    client: MetabaseClient,
    entity: str,
    entity_id_or_query: str,
    prefix: str,
    dashboard_template: str,
) -> JSONValue | None:
    return await automagic_dashboard_path(client, f"{entity}/{entity_id_or_query}/rule/{prefix}/{dashboard_template}")


async def automagic_entity_rule_compare(
    client: MetabaseClient,
    entity: str,
    entity_id_or_query: str,
    prefix: str,
    dashboard_template: str,
    comparison_entity: str,
    comparison_entity_id_or_query: str,
) -> JSONValue | None:
    return await automagic_dashboard_path(
        client,
        f"{entity}/{entity_id_or_query}/rule/{prefix}/{dashboard_template}/compare/{comparison_entity}/{comparison_entity_id_or_query}",
    )


__all__ = [
    "automagic_dashboard_path",
    "automagic_database_candidates",
    "automagic_entity",
    "automagic_entity_cell",
    "automagic_entity_cell_compare",
    "automagic_entity_cell_rule",
    "automagic_entity_cell_rule_compare",
    "automagic_entity_compare",
    "automagic_entity_query_metadata",
    "automagic_entity_rule",
    "automagic_entity_rule_compare",
    "automagic_model_index_primary_key",
]
