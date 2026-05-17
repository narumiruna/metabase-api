from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.timeline import DeleteTimelineResponse
from metabaseapi.endpoints.responses.timeline import ListTimelinesResponse
from metabaseapi.endpoints.responses.timeline import TimelineResponse
from metabaseapi.wire import QueryParamValue


class CreateTimelineRequest(EndpointRequest[TimelineResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/timeline"
    response_model = TimelineResponse


class ListTimelinesRequest(EndpointRequest[ListTimelinesResponse]):
    include: str | None = None
    archived: bool | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/timeline"
    response_model = ListTimelinesResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params: dict[str, QueryParamValue] = {}
        if self.include is not None:
            params["include"] = self.include
        if self.archived is not None:
            params["archived"] = self.archived
        return params


class GetTimelineCollectionRootRequest(EndpointRequest[ListTimelinesResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/timeline/collection/root"
    response_model = ListTimelinesResponse


class GetTimelineCollectionRequest(EndpointRequest[ListTimelinesResponse]):
    collection_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/timeline/collection/{collection_id}"
    response_model = ListTimelinesResponse


class GetTimelineRequest(EndpointRequest[TimelineResponse]):
    timeline_id: int | str
    include: str | None = None
    archived: bool | None = None
    start: str | None = None
    end: str | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/timeline/{timeline_id}"
    response_model = TimelineResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params: dict[str, QueryParamValue] = {}
        if self.include is not None:
            params["include"] = self.include
        if self.archived is not None:
            params["archived"] = self.archived
        if self.start is not None:
            params["start"] = self.start
        if self.end is not None:
            params["end"] = self.end
        return params


class UpdateTimelineRequest(EndpointRequest[TimelineResponse]):
    timeline_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/timeline/{timeline_id}"
    response_model = TimelineResponse


class DeleteTimelineRequest(EndpointRequest[DeleteTimelineResponse]):
    timeline_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/timeline/{timeline_id}"
    response_model = DeleteTimelineResponse
