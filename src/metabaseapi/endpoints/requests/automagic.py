from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.automagic import AutomagicDashboardResponse
from metabaseapi.endpoints.responses.automagic import AutomagicDatabaseCandidatesResponse


class AutomagicDashboardRequest(EndpointRequest[AutomagicDashboardResponse]):
    path: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/automagic-dashboards/{path}"
    response_model = AutomagicDashboardResponse

    def resolve_path(self) -> str:
        return f"/api/automagic-dashboards/{self.path.lstrip('/')}"


class AutomagicDatabaseCandidatesRequest(EndpointRequest[AutomagicDatabaseCandidatesResponse]):
    database_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/automagic-dashboards/database/{database_id}/candidates"
    response_model = AutomagicDatabaseCandidatesResponse


class AutomagicModelIndexPrimaryKeyRequest(EndpointRequest[AutomagicDashboardResponse]):
    model_index_id: int | str
    primary_key_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/automagic-dashboards/model_index/{model_index_id}/primary_key/{primary_key_id}"
    response_model = AutomagicDashboardResponse
