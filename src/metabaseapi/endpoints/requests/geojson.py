from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.geojson import GeojsonByKeyResponse
from metabaseapi.endpoints.responses.geojson import GeojsonResponse
from metabaseapi.wire import QueryParamValue


class GetGeojsonRequest(EndpointRequest[GeojsonResponse]):
    url: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/geojson"
    response_model = GeojsonResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return {"url": self.url}


class GetGeojsonByKeyRequest(EndpointRequest[GeojsonByKeyResponse]):
    key: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/geojson/{key}"
    response_model = GeojsonByKeyResponse
