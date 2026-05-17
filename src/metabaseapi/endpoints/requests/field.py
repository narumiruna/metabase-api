from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.entities import MetabaseField
from metabaseapi.endpoints.execution import EndpointRequest


class GetFieldRequest(EndpointRequest[MetabaseField]):
    field_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/field/{field_id}"
    response_model: ClassVar[object] = MetabaseField

    def resolve_path(self) -> str:
        return f"/api/field/{self.field_id}"
