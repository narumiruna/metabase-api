from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.models import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


class _MetabaseClientRawMixin:
    """Resource-scoped raw mixin for automagic endpoints."""

    async def automagic_database_candidates(self: MetabaseClient, database_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/automagic-dashboards/database/{database_id}/candidates")

    async def automagic_model_index_primary_key(
        self: MetabaseClient,
        model_index_id: int | str,
        primary_key_id: int | str,
    ) -> JSONValue | None:
        return await self.get(f"/api/automagic-dashboards/model_index/{model_index_id}/primary_key/{primary_key_id}")

    async def automagic_dashboard_path(self: MetabaseClient, path: str) -> JSONValue | None:
        return await self.get(f"/api/automagic-dashboards/{path.lstrip('/')}")

    async def automagic_entity(self: MetabaseClient, entity: str, entity_id_or_query: str) -> JSONValue | None:
        return await self.automagic_dashboard_path(f"{entity}/{entity_id_or_query}")

    async def automagic_entity_cell(
        self: MetabaseClient,
        entity: str,
        entity_id_or_query: str,
        cell_query: str,
    ) -> JSONValue | None:
        return await self.automagic_dashboard_path(f"{entity}/{entity_id_or_query}/cell/{cell_query}")

    async def automagic_entity_cell_compare(
        self: MetabaseClient,
        entity: str,
        entity_id_or_query: str,
        cell_query: str,
        comparison_entity: str,
        comparison_entity_id_or_query: str,
    ) -> JSONValue | None:
        return await self.automagic_dashboard_path(
            f"{entity}/{entity_id_or_query}/cell/{cell_query}/compare/{comparison_entity}/{comparison_entity_id_or_query}"
        )

    async def automagic_entity_cell_rule(
        self: MetabaseClient,
        entity: str,
        entity_id_or_query: str,
        cell_query: str,
        prefix: str,
        dashboard_template: str,
    ) -> JSONValue | None:
        return await self.automagic_dashboard_path(
            f"{entity}/{entity_id_or_query}/cell/{cell_query}/rule/{prefix}/{dashboard_template}"
        )

    async def automagic_entity_cell_rule_compare(
        self: MetabaseClient,
        entity: str,
        entity_id_or_query: str,
        cell_query: str,
        prefix: str,
        dashboard_template: str,
        comparison_entity: str,
        comparison_entity_id_or_query: str,
    ) -> JSONValue | None:
        return await self.automagic_dashboard_path(
            f"{entity}/{entity_id_or_query}/cell/{cell_query}/rule/{prefix}/{dashboard_template}/compare/{comparison_entity}/{comparison_entity_id_or_query}"
        )

    async def automagic_entity_compare(
        self: MetabaseClient,
        entity: str,
        entity_id_or_query: str,
        comparison_entity: str,
        comparison_entity_id_or_query: str,
    ) -> JSONValue | None:
        return await self.automagic_dashboard_path(
            f"{entity}/{entity_id_or_query}/compare/{comparison_entity}/{comparison_entity_id_or_query}"
        )

    async def automagic_entity_query_metadata(
        self: MetabaseClient,
        entity: str,
        entity_id_or_query: str,
    ) -> JSONValue | None:
        return await self.automagic_dashboard_path(f"{entity}/{entity_id_or_query}/query_metadata")

    async def automagic_entity_rule(
        self: MetabaseClient,
        entity: str,
        entity_id_or_query: str,
        prefix: str,
        dashboard_template: str,
    ) -> JSONValue | None:
        return await self.automagic_dashboard_path(f"{entity}/{entity_id_or_query}/rule/{prefix}/{dashboard_template}")

    async def automagic_entity_rule_compare(
        self: MetabaseClient,
        entity: str,
        entity_id_or_query: str,
        prefix: str,
        dashboard_template: str,
        comparison_entity: str,
        comparison_entity_id_or_query: str,
    ) -> JSONValue | None:
        return await self.automagic_dashboard_path(
            f"{entity}/{entity_id_or_query}/rule/{prefix}/{dashboard_template}/compare/{comparison_entity}/{comparison_entity_id_or_query}"
        )


__all__ = ["_MetabaseClientRawMixin"]
