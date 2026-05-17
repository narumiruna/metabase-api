from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.entities import Card
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.execution import _ResponseModel
from metabaseapi.endpoints.responses.card import ListCardsResponse
from metabaseapi.endpoints.responses.common import GenericOperationResponse
from metabaseapi.wire import JSONValue


class ListCardsRequest(EndpointRequest[ListCardsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card"
    response_model: ClassVar[_ResponseModel] = ListCardsResponse


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
    response_model: ClassVar[_ResponseModel] = Card

    def request_body(self) -> JSONValue:
        return self.model_dump(exclude_none=True)


class GetCardRequest(EndpointRequest[Card]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}"
    response_model: ClassVar[_ResponseModel] = Card

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}"


class GetCardCollectionsRequest(EndpointRequest[GenericOperationResponse]):
    card_ids: list[int | str] | None = None
    collection_id: int | str | None = None

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/collections"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse

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
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse


class GetCardPublicRequest(EndpointRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/public"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse


class CreateCardPublicLinkRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/public_link"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/public_link"


class DeleteCardPublicLinkRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/public_link"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/public_link"


class UpdateCardRequest(EndpointRequest[Card]):
    card_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}"
    response_model: ClassVar[_ResponseModel] = Card

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}"


class DeleteCardRequest(EndpointRequest[GenericOperationResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}"


class CopyCardRequest(EndpointRequest[Card]):
    card_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/copy"
    response_model: ClassVar[_ResponseModel] = Card

    def resolve_path(self) -> str:
        return f"/api/card/{self.card_id}/copy"

    def request_body(self) -> JSONValue:
        return self.body or None


class MoveCardsRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, object]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/cards/move"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse
