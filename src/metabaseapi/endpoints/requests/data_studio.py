from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.execution import _ResponseModel
from metabaseapi.endpoints.responses.common import GenericOperationResponse


class DataStudioTableDiscardValuesRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/data-studio/table/discard-values"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse


class DataStudioTableEditRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/data-studio/table/edit"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse


class DataStudioTableRescanValuesRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/data-studio/table/rescan-values"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse


class DataStudioTableSelectionRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/data-studio/table/selection"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse


class DataStudioTableSyncSchemaRequest(EndpointRequest[GenericOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/data-studio/table/sync-schema"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse
