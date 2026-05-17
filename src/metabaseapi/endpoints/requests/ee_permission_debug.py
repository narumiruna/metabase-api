from __future__ import annotations

from typing import ClassVar
from typing import cast

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_permission_debug import EePermissionDebugResponse
from metabaseapi.wire import QueryParamValue


class GetEePermissionDebugRequest(EndpointRequest[EePermissionDebugResponse]):
    user_id: int | str
    model_id: int | str
    action_type: str
    extra_params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/permission_debug"
    response_model = EePermissionDebugResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params = dict(self.extra_params)
        params.update(
            {
                "user_id": cast("QueryParamValue", self.user_id),
                "model_id": cast("QueryParamValue", self.model_id),
                "action_type": self.action_type,
            }
        )
        return params
