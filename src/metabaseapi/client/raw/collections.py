from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.models import JSONValue

if TYPE_CHECKING:
    from metabaseapi.client._legacy import MetabaseClient


class _MetabaseClientRawMixin:
    """Resource-scoped raw mixin for collection endpoints."""

    async def list_collections(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/collection")

    async def create_collection(self: MetabaseClient, body: dict[str, object]) -> JSONValue | None:
        return await self.post("/api/collection", body=dict(body))

    async def get_collection(self: MetabaseClient, collection_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/collection/{collection_id}")

    async def update_collection(
        self: MetabaseClient, collection_id: int | str, body: dict[str, object]
    ) -> JSONValue | None:
        return await self.put(f"/api/collection/{collection_id}", body=dict(body))

    async def delete_collection(self: MetabaseClient, collection_id: int | str) -> JSONValue | None:
        return await self.delete(f"/api/collection/{collection_id}")

    async def get_collection_dashboard_question_candidates(
        self: MetabaseClient,
        collection_id: int | str,
    ) -> JSONValue | None:
        return await self.get(f"/api/collection/{collection_id}/dashboard-question-candidates")

    async def get_collection_items(self: MetabaseClient, collection_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/collection/{collection_id}/items")

    async def post_collection_move_dashboard_question_candidates(
        self: MetabaseClient,
        collection_id: int | str,
        body: dict[str, object],
    ) -> JSONValue | None:
        return await self.post(f"/api/collection/{collection_id}/move-dashboard-question-candidates", body=dict(body))

    async def get_collection_graph(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/collection/graph")

    async def put_collection_graph(self: MetabaseClient, body: dict[str, object]) -> JSONValue | None:
        return await self.put("/api/collection/graph", body=dict(body))

    async def get_collection_root(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/collection/root")

    async def get_collection_root_dashboard_question_candidates(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/collection/root/dashboard-question-candidates")

    async def get_collection_root_items(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/collection/root/items")

    async def post_collection_root_move_dashboard_question_candidates(
        self: MetabaseClient,
        body: dict[str, object],
    ) -> JSONValue | None:
        return await self.post("/api/collection/root/move-dashboard-question-candidates", body=dict(body))

    async def get_collection_trash(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/collection/trash")

    async def get_collection_tree(self: MetabaseClient) -> JSONValue | None:
        return await self.get("/api/collection/tree")


__all__ = ["_MetabaseClientRawMixin"]
