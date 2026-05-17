from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.metabase import Collection
from metabaseapi.metabase import CreateCollectionRequest
from metabaseapi.metabase import DeleteCollectionRequest
from metabaseapi.metabase import GenericOperationResponse
from metabaseapi.metabase import GetCollectionDashboardQuestionCandidatesRequest
from metabaseapi.metabase import GetCollectionGraphRequest
from metabaseapi.metabase import GetCollectionItemsRequest
from metabaseapi.metabase import GetCollectionRequest
from metabaseapi.metabase import GetCollectionRootDashboardQuestionCandidatesRequest
from metabaseapi.metabase import GetCollectionRootItemsRequest
from metabaseapi.metabase import GetCollectionRootRequest
from metabaseapi.metabase import GetCollectionTrashRequest
from metabaseapi.metabase import GetCollectionTreeRequest
from metabaseapi.metabase import ListCollectionsRequest
from metabaseapi.metabase import ListCollectionsResponse
from metabaseapi.metabase import PostCollectionMoveDashboardQuestionCandidatesRequest
from metabaseapi.metabase import PostCollectionRootMoveDashboardQuestionCandidatesRequest
from metabaseapi.metabase import PutCollectionGraphRequest
from metabaseapi.metabase import PutCollectionRequest

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


class _MetabaseClientTypedMixin:
    """Resource-scoped typed mixin for collection endpoints."""

    async def list_collections_typed(self: MetabaseClient) -> ListCollectionsResponse:
        return await self.run(ListCollectionsRequest())

    async def create_collection_typed(self: MetabaseClient, body: dict[str, object]) -> Collection:
        return await self.run(CreateCollectionRequest(body=body))

    async def get_collection_typed(self: MetabaseClient, collection_id: int | str) -> Collection:
        return await self.run(GetCollectionRequest(collection_id=collection_id))

    async def update_collection_typed(
        self: MetabaseClient,
        collection_id: int | str,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await self.run(PutCollectionRequest(collection_id=collection_id, body=body))

    async def delete_collection_typed(self: MetabaseClient, collection_id: int | str) -> GenericOperationResponse:
        return await self.run(DeleteCollectionRequest(collection_id=collection_id))

    async def get_collection_dashboard_question_candidates_typed(
        self: MetabaseClient,
        collection_id: int | str,
    ) -> GenericOperationResponse:
        return await self.run(GetCollectionDashboardQuestionCandidatesRequest(collection_id=collection_id))

    async def get_collection_items_typed(self: MetabaseClient, collection_id: int | str) -> GenericOperationResponse:
        return await self.run(GetCollectionItemsRequest(collection_id=collection_id))

    async def post_collection_move_dashboard_question_candidates_typed(
        self: MetabaseClient,
        collection_id: int | str,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await self.run(
            PostCollectionMoveDashboardQuestionCandidatesRequest(collection_id=collection_id, body=body),
        )

    async def get_collection_graph_typed(self: MetabaseClient) -> GenericOperationResponse:
        return await self.run(GetCollectionGraphRequest())

    async def put_collection_graph_typed(self: MetabaseClient, body: dict[str, object]) -> GenericOperationResponse:
        return await self.run(PutCollectionGraphRequest(body=body))

    async def get_collection_root_typed(self: MetabaseClient) -> Collection:
        return await self.run(GetCollectionRootRequest())

    async def get_collection_root_dashboard_question_candidates_typed(self: MetabaseClient) -> GenericOperationResponse:
        return await self.run(GetCollectionRootDashboardQuestionCandidatesRequest())

    async def get_collection_root_items_typed(self: MetabaseClient) -> GenericOperationResponse:
        return await self.run(GetCollectionRootItemsRequest())

    async def post_collection_root_move_dashboard_question_candidates_typed(
        self: MetabaseClient,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await self.run(PostCollectionRootMoveDashboardQuestionCandidatesRequest(body=body))

    async def get_collection_trash_typed(self: MetabaseClient) -> Collection:
        return await self.run(GetCollectionTrashRequest())

    async def get_collection_tree_typed(self: MetabaseClient) -> GenericOperationResponse:
        return await self.run(GetCollectionTreeRequest())


__all__ = ["_MetabaseClientTypedMixin"]
