from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.timeline_event import DeleteTimelineEventResponse
from metabaseapi.endpoints.responses.timeline_event import TimelineEventResponse


class CreateTimelineEventRequest(EndpointRequest[TimelineEventResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/timeline-event"
    response_model = TimelineEventResponse


class GetTimelineEventRequest(EndpointRequest[TimelineEventResponse]):
    event_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/timeline-event/{event_id}"
    response_model = TimelineEventResponse


class UpdateTimelineEventRequest(EndpointRequest[TimelineEventResponse]):
    event_id: int | str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/timeline-event/{event_id}"
    response_model = TimelineEventResponse


class DeleteTimelineEventRequest(EndpointRequest[DeleteTimelineEventResponse]):
    event_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/timeline-event/{event_id}"
    response_model = DeleteTimelineEventResponse
