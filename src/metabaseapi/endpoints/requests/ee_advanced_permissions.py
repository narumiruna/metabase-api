from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_advanced_permissions import DeleteEeImpersonationResponse
from metabaseapi.endpoints.responses.ee_advanced_permissions import EeApplicationPermissionsGraphResponse
from metabaseapi.endpoints.responses.ee_advanced_permissions import EeImpersonationResponse
from metabaseapi.wire import QueryParamValue


class GetEeApplicationPermissionsGraphRequest(EndpointRequest[EeApplicationPermissionsGraphResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/advanced-permissions/application/graph"
    response_model = EeApplicationPermissionsGraphResponse


class PutEeApplicationPermissionsGraphRequest(EndpointRequest[EeApplicationPermissionsGraphResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)
    skip_graph: bool | None = None
    force: bool | None = None

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/ee/advanced-permissions/application/graph"
    response_model = EeApplicationPermissionsGraphResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params: dict[str, QueryParamValue] = {}
        if self.skip_graph is not None:
            params["skip-graph"] = self.skip_graph
        if self.force is not None:
            params["force"] = self.force
        return params


class GetEeImpersonationRequest(EndpointRequest[EeImpersonationResponse]):
    group_id: int | str | None = None
    db_id: int | str | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/advanced-permissions/impersonation"
    response_model = EeImpersonationResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params: dict[str, QueryParamValue] = {}
        if self.group_id is not None:
            params["group_id"] = self.group_id
        if self.db_id is not None:
            params["db_id"] = self.db_id
        return params


class DeleteEeImpersonationRequest(EndpointRequest[DeleteEeImpersonationResponse]):
    impersonation_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/ee/advanced-permissions/impersonation/{impersonation_id}"
    response_model = DeleteEeImpersonationResponse
