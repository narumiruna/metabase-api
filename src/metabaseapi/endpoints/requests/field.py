from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.entities import MetabaseField
from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.field import DeleteFieldDimensionResponse
from metabaseapi.endpoints.responses.field import FieldDimensionResponse
from metabaseapi.endpoints.responses.field import FieldOperationResponse
from metabaseapi.endpoints.responses.field import FieldRelatedResponse
from metabaseapi.endpoints.responses.field import FieldRemappingResponse
from metabaseapi.endpoints.responses.field import FieldSearchResponse
from metabaseapi.endpoints.responses.field import FieldSummaryResponse
from metabaseapi.endpoints.responses.field import FieldValuesResponse
from metabaseapi.endpoints.responses.field import UpdateFieldValuesResponse
from metabaseapi.wire import QueryParamValue


class GetFieldRequest(EndpointRequest[MetabaseField]):
    field_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/field/{field_id}"
    response_model = MetabaseField


class UpdateFieldRequest(EndpointRequest[MetabaseField]):
    field_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/field/{field_id}"
    response_model = MetabaseField


class SetFieldDimensionRequest(EndpointRequest[FieldDimensionResponse]):
    field_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/field/{field_id}/dimension"
    response_model = FieldDimensionResponse


class DeleteFieldDimensionRequest(EndpointRequest[DeleteFieldDimensionResponse]):
    field_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/field/{field_id}/dimension"
    response_model = DeleteFieldDimensionResponse


class DiscardFieldValuesRequest(EndpointRequest[FieldOperationResponse]):
    field_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/field/{field_id}/discard_values"
    response_model = FieldOperationResponse


class GetFieldRelatedRequest(EndpointRequest[FieldRelatedResponse]):
    field_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/field/{field_id}/related"
    response_model = FieldRelatedResponse


class GetFieldRemappingRequest(EndpointRequest[FieldRemappingResponse]):
    field_id: int | str
    remapped_id: int | str
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/field/{field_id}/remapping/{remapped_id}"
    response_model = FieldRemappingResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.params


class RescanFieldValuesRequest(EndpointRequest[FieldOperationResponse]):
    field_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/field/{field_id}/rescan_values"
    response_model = FieldOperationResponse


class SearchFieldValuesRequest(EndpointRequest[FieldSearchResponse]):
    field_id: int | str
    search_id: int | str
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/field/{field_id}/search/{search_id}"
    response_model = FieldSearchResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.params


class GetFieldSummaryRequest(EndpointRequest[FieldSummaryResponse]):
    field_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/field/{field_id}/summary"
    response_model = FieldSummaryResponse


class GetFieldValuesRequest(EndpointRequest[FieldValuesResponse]):
    field_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/field/{field_id}/values"
    response_model = FieldValuesResponse


class UpdateFieldValuesRequest(EndpointRequest[UpdateFieldValuesResponse]):
    field_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/field/{field_id}/values"
    response_model = UpdateFieldValuesResponse
