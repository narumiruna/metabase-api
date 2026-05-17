from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.entities import Card
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.execution import MetabaseRequestClient
from metabaseapi.endpoints.responses.card import CardsDashboardsResponse
from metabaseapi.endpoints.responses.card import ListCardsResponse
from metabaseapi.endpoints.responses.common import GenericOperationResponse
from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue


class ListCardsRequest(EndpointRequest[ListCardsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card"

    async def do(self, client: MetabaseRequestClient) -> ListCardsResponse:
        return await self.execute(client, ListCardsResponse)

    def do_sync(self, client: MetabaseRequestClient) -> ListCardsResponse:
        return self.execute_sync(client, ListCardsResponse)


class CreateCardRequest(EndpointRequest[Card]):
    name: str
    dataset_query: dict[str, Any]
    display: str
    visualization_settings: dict[str, Any] = PydanticField(default_factory=dict)
    type: str | None = "question"
    collection_id: int | str | None = None
    description: str | None = None
    parameters: list[Any] | None = None
    result_metadata: list[Any] | None = None

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card"

    async def do(self, client: MetabaseRequestClient) -> Card:
        return await self.execute(client, Card)

    def do_sync(self, client: MetabaseRequestClient) -> Card:
        return self.execute_sync(client, Card)

    def request_body(self) -> JSONValue:
        return self.model_dump(exclude_none=True)


class GetCardRequest(EndpointRequest[Card]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}"

    async def do(self, client: MetabaseRequestClient) -> Card:
        return await self.execute(client, Card)

    def do_sync(self, client: MetabaseRequestClient) -> Card:
        return self.execute_sync(client, Card)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}"


class GetCardCollectionsRequest(EndpointRequest[GenericOperationResponse]):
    card_ids: list[int | str] | None = None
    collection_id: int | str | None = None

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/collections"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def request_body(self) -> JSONValue:
        body: dict[str, object] = {}
        if self.card_ids is not None:
            body["card_ids"] = self.card_ids
        if self.collection_id is not None:
            body["collection_id"] = self.collection_id
        return body or None


class GetCardEmbeddableRequest(EndpointRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/embeddable"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)


class PostCardPivotQueryRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/pivot/{card-id}/query"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/pivot/{self.card_id}/query"

    def request_body(self) -> JSONValue:
        return self.body or None


class GetCardPublicRequest(EndpointRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/public"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)


class CardParamsSearchRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str
    param_key: str
    query: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/params/{param_key}/search/{query}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/params/{self.param_key}/search/{self.query}"


class CardParamsValuesRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str
    param_key: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/params/{param_key}/values"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/params/{self.param_key}/values"


class CreateCardPublicLinkRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/public_link"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/public_link"


class DeleteCardPublicLinkRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/public_link"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/public_link"


class CardQueryRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/query"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/query"

    def request_body(self) -> JSONValue:
        return self.body or None


class CardQueryExportRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str
    export_format: str
    body: dict[str, Any] = PydanticField(default_factory=dict)
    pivot_results: bool | None = None
    format_rows: bool | None = None

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/query/{export_format}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/query/{self.export_format}"

    def request_body(self) -> JSONValue:
        return self.body or None

    def request_params(self) -> dict[str, QueryParamValue]:
        params: dict[str, QueryParamValue] = {}
        if self.pivot_results is not None:
            params["pivot-results"] = self.pivot_results
        if self.format_rows is not None:
            params["format-rows"] = self.format_rows
        return params


class UpdateCardRequest(EndpointRequest[Card]):
    card_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}"

    async def do(self, client: MetabaseRequestClient) -> Card:
        return await self.execute(client, Card)

    def do_sync(self, client: MetabaseRequestClient) -> Card:
        return self.execute_sync(client, Card)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}"

    def request_body(self) -> JSONValue:
        return self.body


class DeleteCardRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}"


class CopyCardRequest(EndpointRequest[Card]):
    card_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/copy"

    async def do(self, client: MetabaseRequestClient) -> Card:
        return await self.execute(client, Card)

    def do_sync(self, client: MetabaseRequestClient) -> Card:
        return self.execute_sync(client, Card)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/copy"

    def request_body(self) -> JSONValue:
        return self.body or None


class GetCardDashboardsRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/dashboards"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/dashboards"


class CardRemappingRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str
    param_key: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/params/{param_key}/remapping"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/params/{self.param_key}/remapping"


class GetCardQueryMetadataRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/query_metadata"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/query_metadata"


class GetCardSeriesRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/series"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/series"


class CardsDashboardsRequest(EndpointRequest[CardsDashboardsResponse]):
    card_ids: list[int | str]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/cards/dashboards"

    async def do(self, client: MetabaseRequestClient) -> CardsDashboardsResponse:
        return await self.execute(client, CardsDashboardsResponse)

    def do_sync(self, client: MetabaseRequestClient) -> CardsDashboardsResponse:
        return self.execute_sync(client, CardsDashboardsResponse)

    def request_body(self) -> JSONValue:
        return {"card_ids": self.card_ids}


class MoveCardsRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, object]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/cards/move"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def request_body(self) -> JSONValue:
        return self.body
