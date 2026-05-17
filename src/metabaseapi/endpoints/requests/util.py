from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.util import RandomTokenResponse


class GetRandomTokenRequest(EndpointRequest[RandomTokenResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/util/random_token"
    response_model = RandomTokenResponse
