from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.metabase import Card
from metabaseapi.metabase import CardParamsSearchRequest
from metabaseapi.metabase import CardParamsValuesRequest
from metabaseapi.metabase import CardQueryExportRequest
from metabaseapi.metabase import CardQueryRequest
from metabaseapi.metabase import CardRemappingRequest
from metabaseapi.metabase import CardsDashboardsRequest
from metabaseapi.metabase import CardsDashboardsResponse
from metabaseapi.metabase import CopyCardRequest
from metabaseapi.metabase import CreateCardPublicLinkRequest
from metabaseapi.metabase import CreateCardRequest
from metabaseapi.metabase import DeleteCardPublicLinkRequest
from metabaseapi.metabase import DeleteCardRequest
from metabaseapi.metabase import GenericOperationResponse
from metabaseapi.metabase import GetCardCollectionsRequest
from metabaseapi.metabase import GetCardDashboardsRequest
from metabaseapi.metabase import GetCardEmbeddableRequest
from metabaseapi.metabase import GetCardPublicRequest
from metabaseapi.metabase import GetCardQueryMetadataRequest
from metabaseapi.metabase import GetCardRequest
from metabaseapi.metabase import GetCardSeriesRequest
from metabaseapi.metabase import ListCardsRequest
from metabaseapi.metabase import ListCardsResponse
from metabaseapi.metabase import MoveCardsRequest
from metabaseapi.metabase import PostCardPivotQueryRequest
from metabaseapi.metabase import UpdateCardRequest

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


class _MetabaseClientTypedMixin:
    """Resource-scoped typed mixin for card endpoints."""

    async def list_cards_typed(self: MetabaseClient) -> ListCardsResponse:
        return await self.run(ListCardsRequest())

    async def create_card_typed(
        self: MetabaseClient,
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
        return await self.run(request)

    async def create_question_typed(
        self: MetabaseClient,
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
        return await self.create_card_typed(
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

    async def get_card_typed(self: MetabaseClient, card_id: int | str) -> Card:
        return await self.run(GetCardRequest(card_id=card_id))

    async def get_card_collections_typed(
        self: MetabaseClient,
        card_ids: list[int | str],
        collection_id: int | str | None = None,
    ) -> GenericOperationResponse:
        return await self.run(GetCardCollectionsRequest(card_ids=card_ids, collection_id=collection_id))

    async def list_card_embeddable_typed(self: MetabaseClient) -> GenericOperationResponse:
        return await self.run(GetCardEmbeddableRequest())

    async def pivot_card_query_typed(
        self: MetabaseClient,
        card_id: int | str,
        body: dict[str, object] | None = None,
    ) -> GenericOperationResponse:
        return await self.run(PostCardPivotQueryRequest(card_id=card_id, body=body or {}))

    async def list_public_cards_typed(self: MetabaseClient) -> GenericOperationResponse:
        return await self.run(GetCardPublicRequest())

    async def get_card_param_search_values_typed(
        self: MetabaseClient,
        card_id: int | str,
        param_key: str,
        query: str,
    ) -> GenericOperationResponse:
        return await self.run(CardParamsSearchRequest(card_id=card_id, param_key=param_key, query=query))

    async def get_card_param_values_typed(
        self: MetabaseClient, card_id: int | str, param_key: str
    ) -> GenericOperationResponse:
        return await self.run(CardParamsValuesRequest(card_id=card_id, param_key=param_key))

    async def create_card_public_link_typed(self: MetabaseClient, card_id: int | str) -> GenericOperationResponse:
        return await self.run(CreateCardPublicLinkRequest(card_id=card_id))

    async def delete_card_public_link_typed(self: MetabaseClient, card_id: int | str) -> GenericOperationResponse:
        return await self.run(DeleteCardPublicLinkRequest(card_id=card_id))

    async def query_card_typed(
        self: MetabaseClient,
        card_id: int | str,
        body: dict[str, object] | None = None,
    ) -> GenericOperationResponse:
        return await self.run(CardQueryRequest(card_id=card_id, body=body or {}))

    async def query_card_export_typed(
        self: MetabaseClient,
        card_id: int | str,
        export_format: str,
        body: dict[str, object] | None = None,
        *,
        pivot_results: bool | None = None,
        format_rows: bool | None = None,
    ) -> GenericOperationResponse:
        return await self.run(
            CardQueryExportRequest(
                card_id=card_id,
                export_format=export_format,
                body=body or {},
                pivot_results=pivot_results,
                format_rows=format_rows,
            )
        )

    async def cards_dashboards_typed(self: MetabaseClient, card_ids: list[int | str]) -> CardsDashboardsResponse:
        return await self.run(CardsDashboardsRequest(card_ids=card_ids))

    async def move_cards_typed(self: MetabaseClient, body: dict[str, object]) -> GenericOperationResponse:
        return await self.run(MoveCardsRequest(body=body))

    async def update_card_typed(self: MetabaseClient, card_id: int | str, body: dict[str, object]) -> Card:
        return await self.run(UpdateCardRequest(card_id=card_id, body=body))

    async def delete_card_typed(self: MetabaseClient, card_id: int | str) -> GenericOperationResponse:
        return await self.run(DeleteCardRequest(card_id=card_id))

    async def copy_card_typed(self: MetabaseClient, card_id: int | str, body: dict[str, object] | None = None) -> Card:
        return await self.run(CopyCardRequest(card_id=card_id, body=body or {}))

    async def get_card_dashboards_typed(self: MetabaseClient, card_id: int | str) -> GenericOperationResponse:
        return await self.run(GetCardDashboardsRequest(card_id=card_id))

    async def get_card_param_remapping_typed(
        self: MetabaseClient,
        card_id: int | str,
        param_key: str,
    ) -> GenericOperationResponse:
        return await self.run(CardRemappingRequest(card_id=card_id, param_key=param_key))

    async def get_card_query_metadata_typed(self: MetabaseClient, card_id: int | str) -> GenericOperationResponse:
        return await self.run(GetCardQueryMetadataRequest(card_id=card_id))

    async def get_card_series_typed(self: MetabaseClient, card_id: int | str) -> GenericOperationResponse:
        return await self.run(GetCardSeriesRequest(card_id=card_id))


__all__ = ["_MetabaseClientTypedMixin"]
