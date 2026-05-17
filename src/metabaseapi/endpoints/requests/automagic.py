from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.execution import _ResponseModel
from metabaseapi.endpoints.responses.common import GenericOperationResponse


class AutomagicDashboardRequest(EndpointRequest[GenericOperationResponse]):
    path: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/automagic-dashboards/{path}"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse

    def resolve_path(self) -> str:
        return f"/api/automagic-dashboards/{self.path.lstrip('/')}"


class AutomagicDatabaseCandidatesRequest(EndpointRequest[GenericOperationResponse]):
    database_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/automagic-dashboards/database/{database_id}/candidates"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse


class AutomagicModelIndexPrimaryKeyRequest(EndpointRequest[GenericOperationResponse]):
    model_index_id: int | str
    primary_key_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/automagic-dashboards/model_index/{model_index_id}/primary_key/{primary_key_id}"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse
