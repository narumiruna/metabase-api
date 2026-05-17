from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.transform_job import DeleteTransformJobResponse
from metabaseapi.endpoints.responses.transform_job import ListTransformJobsResponse
from metabaseapi.endpoints.responses.transform_job import TransformJobOperationResponse
from metabaseapi.endpoints.responses.transform_job import TransformJobResponse
from metabaseapi.endpoints.responses.transform_job import TransformJobsActiveResponse
from metabaseapi.endpoints.responses.transform_job import TransformJobTransformsResponse
from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue


class CreateTransformJobRequest(EndpointRequest[TransformJobResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/transform-job"
    response_model = TransformJobResponse


class ListTransformJobsRequest(EndpointRequest[ListTransformJobsResponse]):
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/transform-job"
    response_model = ListTransformJobsResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return dict(self.params)


class UpdateTransformJobRequest(EndpointRequest[TransformJobResponse]):
    job_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/transform-job/{job_id}"
    response_model = TransformJobResponse


class UpdateTransformJobsActiveRequest(EndpointRequest[TransformJobsActiveResponse]):
    active: bool

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/transform-job/active"
    response_model = TransformJobsActiveResponse

    def request_body(self) -> JSONValue:
        return {"active": self.active}


class DeleteTransformJobRequest(EndpointRequest[DeleteTransformJobResponse]):
    job_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/transform-job/{job_id}"
    response_model = DeleteTransformJobResponse


class GetTransformJobRequest(EndpointRequest[TransformJobResponse]):
    job_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/transform-job/{job_id}"
    response_model = TransformJobResponse


class RunTransformJobRequest(EndpointRequest[TransformJobOperationResponse]):
    job_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/transform-job/{job_id}/run"
    response_model = TransformJobOperationResponse


class GetTransformJobTransformsRequest(EndpointRequest[TransformJobTransformsResponse]):
    job_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/transform-job/{job_id}/transforms"
    response_model = TransformJobTransformsResponse
