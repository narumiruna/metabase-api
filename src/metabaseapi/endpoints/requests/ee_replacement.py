from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_replacement import EeReplacementCheckReplaceSourceResponse
from metabaseapi.endpoints.responses.ee_replacement import EeReplacementOperationResponse
from metabaseapi.endpoints.responses.ee_replacement import EeReplacementRunResponse
from metabaseapi.endpoints.responses.ee_replacement import EeReplacementRunsResponse
from metabaseapi.wire import QueryParamValue


class PostEeReplacementCheckReplaceSourceRequest(EndpointRequest[EeReplacementCheckReplaceSourceResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/replacement/check-replace-source"
    response_model = EeReplacementCheckReplaceSourceResponse


class PostEeReplacementReplaceModelWithTransformRequest(EndpointRequest[EeReplacementRunResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/replacement/replace-model-with-transform"
    response_model = EeReplacementRunResponse


class PostEeReplacementReplaceSourceRequest(EndpointRequest[EeReplacementRunResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/replacement/replace-source"
    response_model = EeReplacementRunResponse


class GetEeReplacementRunsRequest(EndpointRequest[EeReplacementRunsResponse]):
    is_active: bool | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/replacement/runs"
    response_model = EeReplacementRunsResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        if self.is_active is None:
            return {}
        return {"is-active": self.is_active}


class GetEeReplacementRunsIdRequest(EndpointRequest[EeReplacementRunResponse]):
    id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/replacement/runs/{id}"
    response_model = EeReplacementRunResponse


class PostEeReplacementRunsIdCancelRequest(EndpointRequest[EeReplacementOperationResponse]):
    id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/replacement/runs/{id}/cancel"
    response_model = EeReplacementOperationResponse
