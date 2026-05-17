from __future__ import annotations

from typing import Any
from typing import ClassVar
from typing import cast

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.mt_gtap import MtGtapDeleteResponse
from metabaseapi.endpoints.responses.mt_gtap import MtGtapResponse
from metabaseapi.endpoints.responses.mt_gtap import MtGtapsResponse
from metabaseapi.endpoints.responses.mt_gtap import MtGtapValidationResponse
from metabaseapi.wire import QueryParamValue


class GetMtGtapRequest(EndpointRequest[MtGtapsResponse]):
    group_id: int | str | None = None
    table_id: int | str | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/mt/gtap"
    response_model = MtGtapsResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return {
            key: cast("QueryParamValue", value)
            for key, value in (("group_id", self.group_id), ("table_id", self.table_id))
            if value is not None
        }


class PostMtGtapRequest(EndpointRequest[MtGtapResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/mt/gtap"
    response_model = MtGtapResponse


class PostMtGtapValidateRequest(EndpointRequest[MtGtapValidationResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/mt/gtap/validate"
    response_model = MtGtapValidationResponse


class GetMtGtapIdRequest(EndpointRequest[MtGtapResponse]):
    gtap_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/mt/gtap/{gtap_id}"
    response_model = MtGtapResponse


class PutMtGtapIdRequest(EndpointRequest[MtGtapResponse]):
    gtap_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/mt/gtap/{gtap_id}"
    response_model = MtGtapResponse


class DeleteMtGtapIdRequest(EndpointRequest[MtGtapDeleteResponse]):
    gtap_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/mt/gtap/{gtap_id}"
    response_model = MtGtapDeleteResponse
