from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.model_index import DeleteModelIndexResponse
from metabaseapi.endpoints.responses.model_index import ListModelIndexesResponse
from metabaseapi.endpoints.responses.model_index import ModelIndex


class CreateModelIndexRequest(EndpointRequest[ModelIndex]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/model-index"
    response_model = ModelIndex


class ListModelIndexesRequest(EndpointRequest[ListModelIndexesResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/model-index"
    response_model = ListModelIndexesResponse


class GetModelIndexRequest(EndpointRequest[ModelIndex]):
    id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/model-index/{id}"
    response_model = ModelIndex


class DeleteModelIndexRequest(EndpointRequest[DeleteModelIndexResponse]):
    id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/model-index/{id}"
    response_model = DeleteModelIndexResponse
