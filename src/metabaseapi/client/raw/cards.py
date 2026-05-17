from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING

from metabaseapi.models import JSONValue
from metabaseapi.models import QueryParamValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


class _MetabaseClientRawMixin:
    """Resource-scoped raw mixin for card endpoints."""

    async def list_cards(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/card")

    async def create_card(
        self: MetabaseClient,
        *,
        name: str,
        dataset_query: Mapping[str, object],
        display: str,
        visualization_settings: Mapping[str, object] | None = None,
        card_type: str | None = "question",
        collection_id: int | str | None = None,
        description: str | None = None,
        parameters: list[object] | None = None,
        result_metadata: list[object] | None = None,
    ) -> JSONValue | None:
        body: dict[str, object] = {
            "name": name,
            "dataset_query": dict(dataset_query),
            "display": display,
            "visualization_settings": dict(visualization_settings or {}),
        }
        if card_type is not None:
            body["type"] = card_type
        if collection_id is not None:
            body["collection_id"] = collection_id
        if description is not None:
            body["description"] = description
        if parameters is not None:
            body["parameters"] = parameters
        if result_metadata is not None:
            body["result_metadata"] = result_metadata
        return await self.post("/api/card", body=body)

    async def create_question(
        self: MetabaseClient,
        *,
        name: str,
        dataset_query: Mapping[str, object],
        display: str,
        visualization_settings: Mapping[str, object] | None = None,
        collection_id: int | str | None = None,
        description: str | None = None,
        parameters: list[object] | None = None,
        result_metadata: list[object] | None = None,
    ) -> JSONValue | None:
        return await self.create_card(
            name=name,
            dataset_query=dataset_query,
            display=display,
            visualization_settings=visualization_settings,
            card_type="question",
            collection_id=collection_id,
            description=description,
            parameters=parameters,
            result_metadata=result_metadata,
        )

    async def card_collections(
        self: MetabaseClient,
        card_ids: list[int | str],
        collection_id: int | str | None = None,
    ) -> JSONValue | None:
        body: dict[str, object] = {"card_ids": card_ids}
        if collection_id is not None:
            body["collection_id"] = collection_id
        return await self.post("/api/card/collections", body=body)

    async def list_embeddable_cards(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/card/embeddable")

    async def pivot_query(
        self: MetabaseClient,
        card_id: int | str,
        body: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        return await self.post(f"/api/card/pivot/{card_id}/query", body=dict(body) if body is not None else None)

    async def list_public_cards(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/card/public")

    async def get_card_param_search_values(
        self: MetabaseClient,
        card_id: int | str,
        param_key: str,
        query: str,
    ) -> JSONValue | None:
        return await self.get(f"/api/card/{card_id}/params/{param_key}/search/{query}")

    async def get_card_param_values(self: MetabaseClient, card_id: int | str, param_key: str) -> JSONValue | None:
        return await self.get(f"/api/card/{card_id}/params/{param_key}/values")

    async def create_card_public_link(self: MetabaseClient, card_id: int | str) -> JSONValue | None:
        return await self.post(f"/api/card/{card_id}/public_link")

    async def delete_card_public_link(self: MetabaseClient, card_id: int | str) -> JSONValue | None:
        return await self.delete(f"/api/card/{card_id}/public_link")

    async def query_card(
        self: MetabaseClient,
        card_id: int | str,
        body: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        return await self.post(f"/api/card/{card_id}/query", body=dict(body) if body is not None else None)

    async def query_card_export(
        self: MetabaseClient,
        card_id: int | str,
        export_format: str,
        body: Mapping[str, object] | None = None,
        *,
        pivot_results: bool | None = None,
        format_rows: bool | None = None,
    ) -> JSONValue | None:
        params: dict[str, QueryParamValue] = {}
        if pivot_results is not None:
            params["pivot-results"] = pivot_results
        if format_rows is not None:
            params["format-rows"] = format_rows
        return await self.post(
            f"/api/card/{card_id}/query/{export_format}",
            body=dict(body) if body is not None else None,
            params=params or None,
        )

    async def update_card(self: MetabaseClient, card_id: int | str, body: Mapping[str, object]) -> JSONValue | None:
        return await self.put(f"/api/card/{card_id}", body=dict(body))

    async def delete_card(self: MetabaseClient, card_id: int | str) -> JSONValue | None:
        return await self.delete(f"/api/card/{card_id}")

    async def copy_card(self: MetabaseClient, card_id: int | str) -> JSONValue | None:
        return await self.post(f"/api/card/{card_id}/copy")

    async def cards_dashboards(self: MetabaseClient, card_ids: list[int | str]) -> JSONValue | None:
        return await self.post("/api/cards/dashboards", body={"card_ids": card_ids})

    async def move_cards(self: MetabaseClient, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/cards/move", body=dict(body))

    async def get_card_dashboards(self: MetabaseClient, card_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/card/{card_id}/dashboards")

    async def get_card_param_remapping(self: MetabaseClient, card_id: int | str, param_key: str) -> JSONValue | None:
        return await self.get(f"/api/card/{card_id}/params/{param_key}/remapping")

    async def get_card_query_metadata(self: MetabaseClient, card_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/card/{card_id}/query_metadata")

    async def get_card_series(self: MetabaseClient, card_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/card/{card_id}/series")

    async def get_card(self: MetabaseClient, card_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/card/{card_id}")


__all__ = ["_MetabaseClientRawMixin"]
