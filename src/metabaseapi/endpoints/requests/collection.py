from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.entities import Collection
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.execution import _ResponseModel
from metabaseapi.endpoints.responses.collection import ListCollectionsResponse
from metabaseapi.endpoints.responses.common import GenericOperationResponse


class CreateCollectionRequest(EndpointRequest[Collection]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/collection"
    response_model: ClassVar[_ResponseModel] = Collection


class GetCollectionTreeRequest(EndpointRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/tree"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse


class GetCollectionDashboardQuestionCandidatesRequest(EndpointRequest[GenericOperationResponse]):
    collection_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/{collection_id}/dashboard-question-candidates"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse


class GetCollectionItemsRequest(EndpointRequest[GenericOperationResponse]):
    collection_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/{collection_id}/items"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse


class GetCollectionTrashRequest(EndpointRequest[Collection]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/trash"
    response_model: ClassVar[_ResponseModel] = Collection


class PostCollectionMoveDashboardQuestionCandidatesRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)
    collection_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/collection/{collection_id}/move-dashboard-question-candidates"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse


class ListCollectionsRequest(EndpointRequest[ListCollectionsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection"
    response_model: ClassVar[_ResponseModel] = ListCollectionsResponse


class GetCollectionRequest(EndpointRequest[Collection]):
    collection_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/{collection_id}"
    response_model: ClassVar[_ResponseModel] = Collection


class PutCollectionRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, Any]
    collection_id: int | str

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/collection/{collection_id}"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse


class DeleteCollectionRequest(EndpointRequest[GenericOperationResponse]):
    collection_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/collection/{collection_id}"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse
