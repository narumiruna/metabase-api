from __future__ import annotations

from typing import ClassVar
from typing import cast

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_upload_management import EeUploadManagementDeleteTableResponse
from metabaseapi.endpoints.responses.ee_upload_management import EeUploadManagementTablesResponse
from metabaseapi.wire import QueryParamValue


class GetEeUploadManagementTablesRequest(EndpointRequest[EeUploadManagementTablesResponse]):
    params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/upload-management/tables"
    response_model = EeUploadManagementTablesResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.params


class DeleteEeUploadManagementTablesIdRequest(EndpointRequest[EeUploadManagementDeleteTableResponse]):
    table_id: int | str
    archive_cards: bool | None = None

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/ee/upload-management/tables/{table_id}"
    response_model = EeUploadManagementDeleteTableResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        if self.archive_cards is None:
            return {}
        return {"archive_cards": cast("QueryParamValue", self.archive_cards)}
