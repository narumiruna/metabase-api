from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.measure import ListMeasuresResponse
from metabaseapi.endpoints.responses.measure import Measure
from metabaseapi.endpoints.responses.measure import MeasureDimensionRemappingResponse
from metabaseapi.endpoints.responses.measure import MeasureDimensionSearchResponse
from metabaseapi.endpoints.responses.measure import MeasureDimensionValuesResponse
from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue


class CreateMeasureRequest(EndpointRequest[Measure]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/measure"
    response_model = Measure


class ListMeasuresRequest(EndpointRequest[ListMeasuresResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/measure"
    response_model = ListMeasuresResponse


class GetMeasureRequest(EndpointRequest[Measure]):
    measure_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/measure/{measure_id}"
    response_model = Measure


class UpdateMeasureRequest(EndpointRequest[Measure]):
    measure_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/measure/{measure_id}"
    response_model = Measure


class GetMeasureDimensionRemappingRequest(EndpointRequest[MeasureDimensionRemappingResponse]):
    measure_id: int | str
    dimension_key: str
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/measure/{measure_id}/dimension/{dimension_key}/remapping"
    response_model = MeasureDimensionRemappingResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.params


class SearchMeasureDimensionValuesRequest(EndpointRequest[MeasureDimensionSearchResponse]):
    measure_id: int | str
    dimension_key: str
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/measure/{measure_id}/dimension/{dimension_key}/search"
    response_model = MeasureDimensionSearchResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.params


class GetMeasureDimensionValuesRequest(EndpointRequest[MeasureDimensionValuesResponse]):
    measure_id: int | str
    dimension_key: str
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/measure/{measure_id}/dimension/{dimension_key}/values"
    response_model = MeasureDimensionValuesResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.params

    def request_body(self) -> JSONValue | None:
        return None
