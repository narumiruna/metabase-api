from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.entities import Card
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.metric import ListMetricsResponse
from metabaseapi.endpoints.responses.metric import MetricBreakoutValuesResponse
from metabaseapi.endpoints.responses.metric import MetricDatasetResponse
from metabaseapi.endpoints.responses.metric import MetricDimensionRemappingResponse
from metabaseapi.endpoints.responses.metric import MetricDimensionSearchResponse
from metabaseapi.endpoints.responses.metric import MetricDimensionValuesResponse
from metabaseapi.wire import JSONValue
from metabaseapi.wire import QueryParamValue


class ListMetricsRequest(EndpointRequest[ListMetricsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/metric"
    response_model = ListMetricsResponse


class MetricBreakoutValuesRequest(EndpointRequest[MetricBreakoutValuesResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/metric/breakout-values"
    response_model = MetricBreakoutValuesResponse

    def request_body(self) -> JSONValue:
        return self.body or None


class MetricDatasetRequest(EndpointRequest[MetricDatasetResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/metric/dataset"
    response_model = MetricDatasetResponse

    def request_body(self) -> JSONValue:
        return self.body or None


class GetMetricRequest(EndpointRequest[Card]):
    metric_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/metric/{metric_id}"
    response_model = Card


class GetMetricDimensionRemappingRequest(EndpointRequest[MetricDimensionRemappingResponse]):
    metric_id: int | str
    dimension_key: str
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/metric/{metric_id}/dimension/{dimension_key}/remapping"
    response_model = MetricDimensionRemappingResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.params


class SearchMetricDimensionValuesRequest(EndpointRequest[MetricDimensionSearchResponse]):
    metric_id: int | str
    dimension_key: str
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/metric/{metric_id}/dimension/{dimension_key}/search"
    response_model = MetricDimensionSearchResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.params


class GetMetricDimensionValuesRequest(EndpointRequest[MetricDimensionValuesResponse]):
    metric_id: int | str
    dimension_key: str
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/metric/{metric_id}/dimension/{dimension_key}/values"
    response_model = MetricDimensionValuesResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.params
