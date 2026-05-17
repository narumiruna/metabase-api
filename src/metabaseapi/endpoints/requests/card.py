from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.entities import Card
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.card import CardCollectionsResponse
from metabaseapi.endpoints.responses.card import CardEmbeddableResponse
from metabaseapi.endpoints.responses.card import CardPublicResponse
from metabaseapi.endpoints.responses.card import CreateCardPublicLinkResponse
from metabaseapi.endpoints.responses.card import DeleteCardPublicLinkResponse
from metabaseapi.endpoints.responses.card import DeleteCardResponse
from metabaseapi.endpoints.responses.card import ListCardsResponse
from metabaseapi.endpoints.responses.card import MoveCardsResponse
from metabaseapi.wire import JSONValue


class ListCardsRequest(EndpointRequest[ListCardsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card"
    response_model = ListCardsResponse


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
    response_model = Card

    def request_body(self) -> JSONValue:
        return self.model_dump(exclude_none=True)


class GetCardRequest(EndpointRequest[Card]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}"
    response_model = Card


class GetCardCollectionsRequest(EndpointRequest[CardCollectionsResponse]):
    card_ids: list[int | str] | None = None
    collection_id: int | str | None = None

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/collections"
    response_model = CardCollectionsResponse

    def request_body(self) -> JSONValue:
        body: dict[str, object] = {}
        if self.card_ids is not None:
            body["card_ids"] = self.card_ids
        if self.collection_id is not None:
            body["collection_id"] = self.collection_id
        return body or None


class GetCardEmbeddableRequest(EndpointRequest[CardEmbeddableResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/embeddable"
    response_model = CardEmbeddableResponse


class GetCardPublicRequest(EndpointRequest[CardPublicResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/card/public"
    response_model = CardPublicResponse


class CreateCardPublicLinkRequest(EndpointRequest[CreateCardPublicLinkResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/public_link"
    response_model = CreateCardPublicLinkResponse


class DeleteCardPublicLinkRequest(EndpointRequest[DeleteCardPublicLinkResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/public_link"
    response_model = DeleteCardPublicLinkResponse


class UpdateCardRequest(EndpointRequest[Card]):
    card_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}"
    response_model = Card


class DeleteCardRequest(EndpointRequest[DeleteCardResponse]):
    card_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}"
    response_model = DeleteCardResponse


class CopyCardRequest(EndpointRequest[Card]):
    card_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/card/{card_id}/copy"
    response_model = Card

    def request_body(self) -> JSONValue:
        return self.body or None


class MoveCardsRequest(EndpointRequest[MoveCardsResponse]):
    body: dict[str, object]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/cards/move"
    response_model = MoveCardsResponse
