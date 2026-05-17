from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_transforms import EeTransformInspectQueryResponse
from metabaseapi.endpoints.responses.ee_transforms import EeTransformInspectResponse
from metabaseapi.wire import QueryParamValue


class GetEeTransformsIdInspectRequest(EndpointRequest[EeTransformInspectResponse]):
    transform_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/transforms/{transform_id}/inspect"
    response_model = EeTransformInspectResponse


class GetEeTransformsIdInspectLensIdRequest(EndpointRequest[EeTransformInspectResponse]):
    transform_id: int | str
    lens_id: int | str
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/transforms/{transform_id}/inspect/{lens_id}"
    response_model = EeTransformInspectResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.params


class PostEeTransformsIdInspectLensIdQueryRequest(EndpointRequest[EeTransformInspectQueryResponse]):
    transform_id: int | str
    lens_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/transforms/{transform_id}/inspect/{lens_id}/query"
    response_model = EeTransformInspectQueryResponse
