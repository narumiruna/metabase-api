from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.data_studio import DataStudioTableOperationResponse


class DataStudioTableDiscardValuesRequest(EndpointRequest[DataStudioTableOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/data-studio/table/discard-values"
    response_model = DataStudioTableOperationResponse


class DataStudioTableEditRequest(EndpointRequest[DataStudioTableOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/data-studio/table/edit"
    response_model = DataStudioTableOperationResponse


class DataStudioTableRescanValuesRequest(EndpointRequest[DataStudioTableOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/data-studio/table/rescan-values"
    response_model = DataStudioTableOperationResponse


class DataStudioTableSelectionRequest(EndpointRequest[DataStudioTableOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/data-studio/table/selection"
    response_model = DataStudioTableOperationResponse


class DataStudioTableSyncSchemaRequest(EndpointRequest[DataStudioTableOperationResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/data-studio/table/sync-schema"
    response_model = DataStudioTableOperationResponse
