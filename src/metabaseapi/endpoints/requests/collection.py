from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.entities import Collection
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.collection import ListCollectionsResponse
from metabaseapi.endpoints.responses.common import GenericOperationResponse
from metabaseapi.wire import JSONValue


class CreateCollectionRequest(EndpointRequest[Collection]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/collection"
    response_model: ClassVar[object] = Collection

    def request_body(self) -> JSONValue:
        return self.body


class GetCollectionTreeRequest(EndpointRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/tree"
    response_model: ClassVar[object] = GenericOperationResponse


class GetCollectionDashboardQuestionCandidatesRequest(EndpointRequest[GenericOperationResponse]):
    collection_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/{collection_id}/dashboard-question-candidates"
    response_model: ClassVar[object] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/collection/{self.collection_id}/dashboard-question-candidates"


class GetCollectionItemsRequest(EndpointRequest[GenericOperationResponse]):
    collection_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/{collection_id}/items"
    response_model: ClassVar[object] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/collection/{self.collection_id}/items"


class GetCollectionTrashRequest(EndpointRequest[Collection]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/trash"
    response_model: ClassVar[object] = Collection


class PostCollectionMoveDashboardQuestionCandidatesRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)
    collection_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/collection/{collection_id}/move-dashboard-question-candidates"
    response_model: ClassVar[object] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/collection/{self.collection_id}/move-dashboard-question-candidates"

    def request_body(self) -> JSONValue:
        return self.body


class ListCollectionsRequest(EndpointRequest[ListCollectionsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection"
    response_model: ClassVar[object] = ListCollectionsResponse


class GetCollectionRequest(EndpointRequest[Collection]):
    collection_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/{collection_id}"
    response_model: ClassVar[object] = Collection

    def resolve_path(self) -> str:
        return f"/api/collection/{self.collection_id}"


class PutCollectionRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, Any]
    collection_id: int | str

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/collection/{collection_id}"
    response_model: ClassVar[object] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/collection/{self.collection_id}"

    def request_body(self) -> JSONValue:
        return self.body


class DeleteCollectionRequest(EndpointRequest[GenericOperationResponse]):
    collection_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/collection/{collection_id}"
    response_model: ClassVar[object] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/collection/{self.collection_id}"
