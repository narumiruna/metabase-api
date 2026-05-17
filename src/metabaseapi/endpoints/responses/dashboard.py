from __future__ import annotations

from typing import Any

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field as PydanticField
from pydantic import model_validator

from metabaseapi.endpoints._response_payload import normalize_strict_list_payload
from metabaseapi.endpoints._response_payload import normalize_unstructured_payload
from metabaseapi.endpoints.entities import Dashboard
from metabaseapi.wire import JSONValue


class ListDashboardsResponse(BaseModel):
    dashboards: list[Dashboard] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "dashboards")


class _DashboardOperationResponse(BaseModel):
    raw: JSONValue | None = None
    model_config = ConfigDict(extra="allow")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_unstructured_payload(values)


class DashboardEmbeddableResponse(BaseModel):
    dashboards: list[Dashboard] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "dashboards")


class DashboardPublicResponse(DashboardEmbeddableResponse):
    pass


class SaveDashboardResponse(_DashboardOperationResponse):
    pass


class SaveDashboardToCollectionResponse(_DashboardOperationResponse):
    pass


class CreateDashboardPublicLinkResponse(_DashboardOperationResponse):
    uuid: str | None = None


class DeleteDashboardPublicLinkResponse(_DashboardOperationResponse):
    ok: bool | None = None


class DeleteDashboardResponse(_DashboardOperationResponse):
    ok: bool | None = None


class UpdateDashboardCardsResponse(_DashboardOperationResponse):
    ok: bool | None = None


class DashboardItemsResponse(BaseModel):
    items: list[JSONValue] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "items")


class DashboardQueryResponse(_DashboardOperationResponse):
    pass


class DashboardQueryExportResponse(_DashboardOperationResponse):
    pass


class DashboardParameterValuesResponse(BaseModel):
    values: list[JSONValue] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "values")


class DashboardRemappingResponse(_DashboardOperationResponse):
    pass


class DashboardQueryMetadataResponse(_DashboardOperationResponse):
    pass


class DashboardRelatedResponse(DashboardItemsResponse):
    pass


class DashboardValidFilterFieldsResponse(BaseModel):
    fields: list[JSONValue] = PydanticField(default_factory=list)
    model_config = ConfigDict(extra="forbid")

    @model_validator(mode="before")
    @classmethod
    def normalize_payload(cls, values: object) -> dict[str, Any]:
        return normalize_strict_list_payload(values, "fields")
