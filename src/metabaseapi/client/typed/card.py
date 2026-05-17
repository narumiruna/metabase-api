from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.endpoints.entities import Card
from metabaseapi.endpoints.requests.card import CardParamsSearchRequest
from metabaseapi.endpoints.requests.card import CardParamsValuesRequest
from metabaseapi.endpoints.requests.card import CardQueryExportRequest
from metabaseapi.endpoints.requests.card import CardQueryRequest
from metabaseapi.endpoints.requests.card import CardRemappingRequest
from metabaseapi.endpoints.requests.card import CardsDashboardsRequest
from metabaseapi.endpoints.requests.card import CopyCardRequest
from metabaseapi.endpoints.requests.card import CreateCardPublicLinkRequest
from metabaseapi.endpoints.requests.card import CreateCardRequest
from metabaseapi.endpoints.requests.card import DeleteCardPublicLinkRequest
from metabaseapi.endpoints.requests.card import DeleteCardRequest
from metabaseapi.endpoints.requests.card import GetCardCollectionsRequest
from metabaseapi.endpoints.requests.card import GetCardDashboardsRequest
from metabaseapi.endpoints.requests.card import GetCardEmbeddableRequest
from metabaseapi.endpoints.requests.card import GetCardPublicRequest
from metabaseapi.endpoints.requests.card import GetCardQueryMetadataRequest
from metabaseapi.endpoints.requests.card import GetCardRequest
from metabaseapi.endpoints.requests.card import GetCardSeriesRequest
from metabaseapi.endpoints.requests.card import ListCardsRequest
from metabaseapi.endpoints.requests.card import MoveCardsRequest
from metabaseapi.endpoints.requests.card import PostCardPivotQueryRequest
from metabaseapi.endpoints.requests.card import UpdateCardRequest
from metabaseapi.endpoints.responses import CardsDashboardsResponse
from metabaseapi.endpoints.responses import GenericOperationResponse
from metabaseapi.endpoints.responses import ListCardsResponse

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def list_cards_typed(client: MetabaseClient) -> ListCardsResponse:
    return await client.run(ListCardsRequest())


async def create_card_typed(
    client: MetabaseClient,
    *,
    name: str,
    dataset_query: dict[str, object],
    display: str,
    visualization_settings: dict[str, object] | None = None,
    card_type: str | None = "question",
    collection_id: int | str | None = None,
    description: str | None = None,
    parameters: list[object] | None = None,
    result_metadata: list[object] | None = None,
) -> Card:
    request = CreateCardRequest(
        name=name,
        dataset_query=dataset_query,
        display=display,
        visualization_settings=visualization_settings or {},
        type=card_type,
        collection_id=collection_id,
        description=description,
        parameters=parameters,
        result_metadata=result_metadata,
    )
    return await client.run(request)


async def create_question_typed(
    client: MetabaseClient,
    *,
    name: str,
    dataset_query: dict[str, object],
    display: str,
    visualization_settings: dict[str, object] | None = None,
    collection_id: int | str | None = None,
    description: str | None = None,
    parameters: list[object] | None = None,
    result_metadata: list[object] | None = None,
) -> Card:
    return await client.create_card_typed(
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


async def get_card_typed(client: MetabaseClient, card_id: int | str) -> Card:
    return await client.run(GetCardRequest(card_id=card_id))


async def get_card_collections_typed(
    client: MetabaseClient,
    card_ids: list[int | str],
    collection_id: int | str | None = None,
) -> GenericOperationResponse:
    return await client.run(GetCardCollectionsRequest(card_ids=card_ids, collection_id=collection_id))


async def list_card_embeddable_typed(client: MetabaseClient) -> GenericOperationResponse:
    return await client.run(GetCardEmbeddableRequest())


async def pivot_card_query_typed(
    client: MetabaseClient,
    card_id: int | str,
    body: dict[str, object] | None = None,
) -> GenericOperationResponse:
    return await client.run(PostCardPivotQueryRequest(card_id=card_id, body=body or {}))


async def list_public_cards_typed(client: MetabaseClient) -> GenericOperationResponse:
    return await client.run(GetCardPublicRequest())


async def get_card_param_search_values_typed(
    client: MetabaseClient,
    card_id: int | str,
    param_key: str,
    query: str,
) -> GenericOperationResponse:
    return await client.run(CardParamsSearchRequest(card_id=card_id, param_key=param_key, query=query))


async def get_card_param_values_typed(
    client: MetabaseClient, card_id: int | str, param_key: str
) -> GenericOperationResponse:
    return await client.run(CardParamsValuesRequest(card_id=card_id, param_key=param_key))


async def create_card_public_link_typed(client: MetabaseClient, card_id: int | str) -> GenericOperationResponse:
    return await client.run(CreateCardPublicLinkRequest(card_id=card_id))


async def delete_card_public_link_typed(client: MetabaseClient, card_id: int | str) -> GenericOperationResponse:
    return await client.run(DeleteCardPublicLinkRequest(card_id=card_id))


async def query_card_typed(
    client: MetabaseClient,
    card_id: int | str,
    body: dict[str, object] | None = None,
) -> GenericOperationResponse:
    return await client.run(CardQueryRequest(card_id=card_id, body=body or {}))


async def query_card_export_typed(
    client: MetabaseClient,
    card_id: int | str,
    export_format: str,
    body: dict[str, object] | None = None,
    *,
    pivot_results: bool | None = None,
    format_rows: bool | None = None,
) -> GenericOperationResponse:
    return await client.run(
        CardQueryExportRequest(
            card_id=card_id,
            export_format=export_format,
            body=body or {},
            pivot_results=pivot_results,
            format_rows=format_rows,
        )
    )


async def cards_dashboards_typed(client: MetabaseClient, card_ids: list[int | str]) -> CardsDashboardsResponse:
    return await client.run(CardsDashboardsRequest(card_ids=card_ids))


async def move_cards_typed(client: MetabaseClient, body: dict[str, object]) -> GenericOperationResponse:
    return await client.run(MoveCardsRequest(body=body))


async def update_card_typed(client: MetabaseClient, card_id: int | str, body: dict[str, object]) -> Card:
    return await client.run(UpdateCardRequest(card_id=card_id, body=body))


async def delete_card_typed(client: MetabaseClient, card_id: int | str) -> GenericOperationResponse:
    return await client.run(DeleteCardRequest(card_id=card_id))


async def copy_card_typed(client: MetabaseClient, card_id: int | str, body: dict[str, object] | None = None) -> Card:
    return await client.run(CopyCardRequest(card_id=card_id, body=body or {}))


async def get_card_dashboards_typed(client: MetabaseClient, card_id: int | str) -> GenericOperationResponse:
    return await client.run(GetCardDashboardsRequest(card_id=card_id))


async def get_card_param_remapping_typed(
    client: MetabaseClient,
    card_id: int | str,
    param_key: str,
) -> GenericOperationResponse:
    return await client.run(CardRemappingRequest(card_id=card_id, param_key=param_key))


async def get_card_query_metadata_typed(client: MetabaseClient, card_id: int | str) -> GenericOperationResponse:
    return await client.run(GetCardQueryMetadataRequest(card_id=card_id))


async def get_card_series_typed(client: MetabaseClient, card_id: int | str) -> GenericOperationResponse:
    return await client.run(GetCardSeriesRequest(card_id=card_id))


__all__ = [
    "cards_dashboards_typed",
    "copy_card_typed",
    "create_card_public_link_typed",
    "create_card_typed",
    "create_question_typed",
    "delete_card_public_link_typed",
    "delete_card_typed",
    "get_card_collections_typed",
    "get_card_dashboards_typed",
    "get_card_param_remapping_typed",
    "get_card_param_search_values_typed",
    "get_card_param_values_typed",
    "get_card_query_metadata_typed",
    "get_card_series_typed",
    "get_card_typed",
    "list_card_embeddable_typed",
    "list_cards_typed",
    "list_public_cards_typed",
    "move_cards_typed",
    "pivot_card_query_typed",
    "query_card_export_typed",
    "query_card_typed",
    "update_card_typed",
]
