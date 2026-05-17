from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.product_feedback import ProductFeedbackResponse


class CreateProductFeedbackRequest(EndpointRequest[ProductFeedbackResponse]):
    body: dict[str, object]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/product-feedback"
    response_model = ProductFeedbackResponse
