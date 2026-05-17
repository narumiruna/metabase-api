from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.entities import Collection
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.collection import CollectionDashboardQuestionCandidatesResponse
from metabaseapi.endpoints.responses.collection import CollectionMoveDashboardQuestionCandidatesResponse
from metabaseapi.endpoints.responses.common import GenericOperationResponse


class GetCollectionRootRequest(EndpointRequest[Collection]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/root"
    response_model = Collection


class GetCollectionRootDashboardQuestionCandidatesRequest(
    EndpointRequest[CollectionDashboardQuestionCandidatesResponse]
):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/root/dashboard-question-candidates"
    response_model = CollectionDashboardQuestionCandidatesResponse


class GetCollectionRootItemsRequest(EndpointRequest[GenericOperationResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/collection/root/items"
    response_model = GenericOperationResponse


class PostCollectionRootMoveDashboardQuestionCandidatesRequest(
    EndpointRequest[CollectionMoveDashboardQuestionCandidatesResponse]
):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/collection/root/move-dashboard-question-candidates"
    response_model = CollectionMoveDashboardQuestionCandidatesResponse
