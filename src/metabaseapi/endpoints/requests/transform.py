from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.transform import DeleteTransformResponse
from metabaseapi.endpoints.responses.transform import ListTransformRunsResponse
from metabaseapi.endpoints.responses.transform import ListTransformsResponse
from metabaseapi.endpoints.responses.transform import TransformDependenciesResponse
from metabaseapi.endpoints.responses.transform import TransformOperationResponse
from metabaseapi.endpoints.responses.transform import TransformResponse
from metabaseapi.endpoints.responses.transform import TransformRunResponse
from metabaseapi.wire import QueryParamValue


class ListTransformsRequest(EndpointRequest[ListTransformsResponse]):
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/transform"
    response_model = ListTransformsResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return dict(self.params)


class CreateTransformRequest(EndpointRequest[TransformResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/transform"
    response_model = TransformResponse


class ListTransformRunsRequest(EndpointRequest[ListTransformRunsResponse]):
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/transform/run"
    response_model = ListTransformRunsResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return dict(self.params)


class GetTransformRunRequest(EndpointRequest[TransformRunResponse]):
    run_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/transform/run/{run_id}"
    response_model = TransformRunResponse


class GetTransformRequest(EndpointRequest[TransformResponse]):
    id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/transform/{id}"
    response_model = TransformResponse


class UpdateTransformRequest(EndpointRequest[TransformResponse]):
    id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/transform/{id}"
    response_model = TransformResponse


class DeleteTransformRequest(EndpointRequest[DeleteTransformResponse]):
    id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/transform/{id}"
    response_model = DeleteTransformResponse


class CancelTransformRequest(EndpointRequest[TransformOperationResponse]):
    id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/transform/{id}/cancel"
    response_model = TransformOperationResponse


class GetTransformDependenciesRequest(EndpointRequest[TransformDependenciesResponse]):
    id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/transform/{id}/dependencies"
    response_model = TransformDependenciesResponse


class ResetTransformCheckpointRequest(EndpointRequest[TransformOperationResponse]):
    id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/transform/{id}/reset-checkpoint"
    response_model = TransformOperationResponse


class RunTransformRequest(EndpointRequest[TransformOperationResponse]):
    id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/transform/{id}/run"
    response_model = TransformOperationResponse


class DeleteTransformTableRequest(EndpointRequest[TransformOperationResponse]):
    id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/transform/{id}/table"
    response_model = TransformOperationResponse
