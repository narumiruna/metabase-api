from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.transform_tag import DeleteTransformTagResponse
from metabaseapi.endpoints.responses.transform_tag import ListTransformTagsResponse
from metabaseapi.endpoints.responses.transform_tag import TransformTagResponse
from metabaseapi.wire import QueryParamValue


class CreateTransformTagRequest(EndpointRequest[TransformTagResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/transform-tag"
    response_model = TransformTagResponse


class ListTransformTagsRequest(EndpointRequest[ListTransformTagsResponse]):
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/transform-tag"
    response_model = ListTransformTagsResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return dict(self.params)


class UpdateTransformTagRequest(EndpointRequest[TransformTagResponse]):
    tag_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/transform-tag/{tag_id}"
    response_model = TransformTagResponse


class DeleteTransformTagRequest(EndpointRequest[DeleteTransformTagResponse]):
    tag_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/transform-tag/{tag_id}"
    response_model = DeleteTransformTagResponse
