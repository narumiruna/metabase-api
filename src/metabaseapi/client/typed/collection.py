from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.endpoints.entities import Collection
from metabaseapi.endpoints.requests.collection import CreateCollectionRequest
from metabaseapi.endpoints.requests.collection import DeleteCollectionRequest
from metabaseapi.endpoints.requests.collection import GetCollectionDashboardQuestionCandidatesRequest
from metabaseapi.endpoints.requests.collection import GetCollectionGraphRequest
from metabaseapi.endpoints.requests.collection import GetCollectionItemsRequest
from metabaseapi.endpoints.requests.collection import GetCollectionRequest
from metabaseapi.endpoints.requests.collection import GetCollectionRootDashboardQuestionCandidatesRequest
from metabaseapi.endpoints.requests.collection import GetCollectionRootItemsRequest
from metabaseapi.endpoints.requests.collection import GetCollectionRootRequest
from metabaseapi.endpoints.requests.collection import GetCollectionTrashRequest
from metabaseapi.endpoints.requests.collection import GetCollectionTreeRequest
from metabaseapi.endpoints.requests.collection import ListCollectionsRequest
from metabaseapi.endpoints.requests.collection import PostCollectionMoveDashboardQuestionCandidatesRequest
from metabaseapi.endpoints.requests.collection import PostCollectionRootMoveDashboardQuestionCandidatesRequest
from metabaseapi.endpoints.requests.collection import PutCollectionGraphRequest
from metabaseapi.endpoints.requests.collection import PutCollectionRequest
from metabaseapi.endpoints.responses import GenericOperationResponse
from metabaseapi.endpoints.responses import ListCollectionsResponse

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def list_collections_typed(client: MetabaseClient) -> ListCollectionsResponse:
    return await client.run(ListCollectionsRequest())


async def create_collection_typed(client: MetabaseClient, body: dict[str, object]) -> Collection:
    return await client.run(CreateCollectionRequest(body=body))


async def get_collection_typed(client: MetabaseClient, collection_id: int | str) -> Collection:
    return await client.run(GetCollectionRequest(collection_id=collection_id))


async def update_collection_typed(
    client: MetabaseClient,
    collection_id: int | str,
    body: dict[str, object],
) -> GenericOperationResponse:
    return await client.run(PutCollectionRequest(collection_id=collection_id, body=body))


async def delete_collection_typed(client: MetabaseClient, collection_id: int | str) -> GenericOperationResponse:
    return await client.run(DeleteCollectionRequest(collection_id=collection_id))


async def get_collection_dashboard_question_candidates_typed(
    client: MetabaseClient,
    collection_id: int | str,
) -> GenericOperationResponse:
    return await client.run(GetCollectionDashboardQuestionCandidatesRequest(collection_id=collection_id))


async def get_collection_items_typed(client: MetabaseClient, collection_id: int | str) -> GenericOperationResponse:
    return await client.run(GetCollectionItemsRequest(collection_id=collection_id))


async def post_collection_move_dashboard_question_candidates_typed(
    client: MetabaseClient,
    collection_id: int | str,
    body: dict[str, object],
) -> GenericOperationResponse:
    return await client.run(
        PostCollectionMoveDashboardQuestionCandidatesRequest(collection_id=collection_id, body=body),
    )


async def get_collection_graph_typed(client: MetabaseClient) -> GenericOperationResponse:
    return await client.run(GetCollectionGraphRequest())


async def put_collection_graph_typed(client: MetabaseClient, body: dict[str, object]) -> GenericOperationResponse:
    return await client.run(PutCollectionGraphRequest(body=body))


async def get_collection_root_typed(client: MetabaseClient) -> Collection:
    return await client.run(GetCollectionRootRequest())


async def get_collection_root_dashboard_question_candidates_typed(client: MetabaseClient) -> GenericOperationResponse:
    return await client.run(GetCollectionRootDashboardQuestionCandidatesRequest())


async def get_collection_root_items_typed(client: MetabaseClient) -> GenericOperationResponse:
    return await client.run(GetCollectionRootItemsRequest())


async def post_collection_root_move_dashboard_question_candidates_typed(
    client: MetabaseClient,
    body: dict[str, object],
) -> GenericOperationResponse:
    return await client.run(PostCollectionRootMoveDashboardQuestionCandidatesRequest(body=body))


async def get_collection_trash_typed(client: MetabaseClient) -> Collection:
    return await client.run(GetCollectionTrashRequest())


async def get_collection_tree_typed(client: MetabaseClient) -> GenericOperationResponse:
    return await client.run(GetCollectionTreeRequest())


__all__ = [
    "create_collection_typed",
    "delete_collection_typed",
    "get_collection_dashboard_question_candidates_typed",
    "get_collection_graph_typed",
    "get_collection_items_typed",
    "get_collection_root_dashboard_question_candidates_typed",
    "get_collection_root_items_typed",
    "get_collection_root_typed",
    "get_collection_trash_typed",
    "get_collection_tree_typed",
    "get_collection_typed",
    "list_collections_typed",
    "post_collection_move_dashboard_question_candidates_typed",
    "post_collection_root_move_dashboard_question_candidates_typed",
    "put_collection_graph_typed",
    "update_collection_typed",
]
