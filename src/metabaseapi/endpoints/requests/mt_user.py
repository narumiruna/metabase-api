from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.mt_user import MtUserAttributesResponse
from metabaseapi.endpoints.responses.mt_user import MtUserUpdateAttributesResponse


class GetMtUserAttributesRequest(EndpointRequest[MtUserAttributesResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/mt/user/attributes"
    response_model = MtUserAttributesResponse


class PutMtUserIdAttributesRequest(EndpointRequest[MtUserUpdateAttributesResponse]):
    user_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/mt/user/{user_id}/attributes"
    response_model = MtUserUpdateAttributesResponse
