from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.segment import DeleteSegmentResponse
from metabaseapi.endpoints.responses.segment import ListSegmentsResponse
from metabaseapi.endpoints.responses.segment import Segment
from metabaseapi.endpoints.responses.segment import SegmentRelatedResponse


class CreateSegmentRequest(EndpointRequest[Segment]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/segment"
    response_model = Segment


class ListSegmentsRequest(EndpointRequest[ListSegmentsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/segment"
    response_model = ListSegmentsResponse


class GetSegmentRequest(EndpointRequest[Segment]):
    segment_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/segment/{segment_id}"
    response_model = Segment


class UpdateSegmentRequest(EndpointRequest[Segment]):
    segment_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/segment/{segment_id}"
    response_model = Segment


class DeleteSegmentRequest(EndpointRequest[DeleteSegmentResponse]):
    segment_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/segment/{segment_id}"
    response_model = DeleteSegmentResponse


class GetSegmentRelatedRequest(EndpointRequest[SegmentRelatedResponse]):
    segment_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/segment/{segment_id}/related"
    response_model = SegmentRelatedResponse
