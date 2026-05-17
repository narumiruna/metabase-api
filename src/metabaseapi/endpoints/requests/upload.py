from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.upload import UploadCsvResponse


class UploadCsvRequest(EndpointRequest[UploadCsvResponse]):
    body: dict[str, object]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/upload/csv"
    response_model = UploadCsvResponse
