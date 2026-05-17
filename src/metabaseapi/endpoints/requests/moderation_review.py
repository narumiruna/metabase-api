from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.moderation_review import ModerationReviewResponse


class CreateModerationReviewRequest(EndpointRequest[ModerationReviewResponse]):
    body: dict[str, object]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/moderation-review"
    response_model = ModerationReviewResponse
