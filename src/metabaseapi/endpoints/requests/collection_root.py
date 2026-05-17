from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.entities import Collection
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.execution import ResponseModel
from metabaseapi.endpoints.responses.common import GenericOperationResponse
from metabaseapi.wire import JSONValue


class GetCollectionRootRequest(EndpointRequest[Collection]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/root"
    response_model: ClassVar[ResponseModel] = Collection


class GetCollectionRootDashboardQuestionCandidatesRequest(EndpointRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/root/dashboard-question-candidates"
    response_model: ClassVar[ResponseModel] = GenericOperationResponse


class GetCollectionRootItemsRequest(EndpointRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/root/items"
    response_model: ClassVar[ResponseModel] = GenericOperationResponse


class PostCollectionRootMoveDashboardQuestionCandidatesRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/collection/root/move-dashboard-question-candidates"
    response_model: ClassVar[ResponseModel] = GenericOperationResponse

    def request_body(self) -> JSONValue:
        return self.body
