from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_email import DeleteEeEmailOverrideResponse
from metabaseapi.endpoints.responses.ee_email import EeEmailOverrideResponse


class PutEeEmailOverrideRequest(EndpointRequest[EeEmailOverrideResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/ee/email/override"
    response_model = EeEmailOverrideResponse


class DeleteEeEmailOverrideRequest(EndpointRequest[DeleteEeEmailOverrideResponse]):
    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/ee/email/override"
    response_model = DeleteEeEmailOverrideResponse
