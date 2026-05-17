from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.dataset import DatasetExportResponse
from metabaseapi.endpoints.responses.dataset import DatasetNativeResponse
from metabaseapi.endpoints.responses.dataset import DatasetParameterRemappingResponse
from metabaseapi.endpoints.responses.dataset import DatasetParameterSearchResponse
from metabaseapi.endpoints.responses.dataset import DatasetParameterValuesResponse
from metabaseapi.endpoints.responses.dataset import DatasetPivotResponse
from metabaseapi.endpoints.responses.dataset import DatasetQueryMetadataResponse
from metabaseapi.endpoints.responses.dataset import DatasetQueryResponse
from metabaseapi.wire import JSONValue


class DatasetQueryRequest(EndpointRequest[DatasetQueryResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dataset"
    response_model = DatasetQueryResponse

    def request_body(self) -> JSONValue:
        return self.body or None


class DatasetNativeRequest(EndpointRequest[DatasetNativeResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dataset/native"
    response_model = DatasetNativeResponse

    def request_body(self) -> JSONValue:
        return self.body or None


class DatasetParameterRemappingRequest(EndpointRequest[DatasetParameterRemappingResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dataset/parameter/remapping"
    response_model = DatasetParameterRemappingResponse

    def request_body(self) -> JSONValue:
        return self.body or None


class DatasetParameterSearchRequest(EndpointRequest[DatasetParameterSearchResponse]):
    query: str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dataset/parameter/search/{query}"
    response_model = DatasetParameterSearchResponse

    def request_body(self) -> JSONValue:
        return self.body or None


class DatasetParameterValuesRequest(EndpointRequest[DatasetParameterValuesResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dataset/parameter/values"
    response_model = DatasetParameterValuesResponse

    def request_body(self) -> JSONValue:
        return self.body or None


class DatasetPivotRequest(EndpointRequest[DatasetPivotResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dataset/pivot"
    response_model = DatasetPivotResponse

    def request_body(self) -> JSONValue:
        return self.body or None


class DatasetQueryMetadataRequest(EndpointRequest[DatasetQueryMetadataResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dataset/query_metadata"
    response_model = DatasetQueryMetadataResponse

    def request_body(self) -> JSONValue:
        return self.body or None


class DatasetExportRequest(EndpointRequest[DatasetExportResponse]):
    export_format: str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/dataset/{export_format}"
    response_model = DatasetExportResponse

    def request_body(self) -> JSONValue:
        return self.body or None
