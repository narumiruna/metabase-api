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


class AutomagicEntityRequest(EndpointRequest[AutomagicDashboardResponse]):
    entity: str
    entity_id_or_query: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/automagic-dashboards/{entity}/{entity_id_or_query}"
    response_model = AutomagicDashboardResponse


class AutomagicEntityCellRequest(EndpointRequest[AutomagicDashboardResponse]):
    entity: str
    entity_id_or_query: str
    cell_query: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/automagic-dashboards/{entity}/{entity_id_or_query}/cell/{cell_query}"
    response_model = AutomagicDashboardResponse


class AutomagicEntityCellCompareRequest(EndpointRequest[AutomagicDashboardResponse]):
    entity: str
    entity_id_or_query: str
    cell_query: str
    comparison_entity: str
    comparison_entity_id_or_query: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = (
        "/api/automagic-dashboards/{entity}/{entity_id_or_query}/cell/{cell_query}/compare/"
        "{comparison_entity}/{comparison_entity_id_or_query}"
    )
    response_model = AutomagicDashboardResponse


class AutomagicEntityCellRuleRequest(EndpointRequest[AutomagicDashboardResponse]):
    entity: str
    entity_id_or_query: str
    cell_query: str
    prefix: str
    dashboard_template: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = (
        "/api/automagic-dashboards/{entity}/{entity_id_or_query}/cell/{cell_query}/rule/{prefix}/{dashboard_template}"
    )
    response_model = AutomagicDashboardResponse


class AutomagicEntityCellRuleCompareRequest(EndpointRequest[AutomagicDashboardResponse]):
    entity: str
    entity_id_or_query: str
    cell_query: str
    prefix: str
    dashboard_template: str
    comparison_entity: str
    comparison_entity_id_or_query: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = (
        "/api/automagic-dashboards/{entity}/{entity_id_or_query}/cell/{cell_query}/rule/"
        "{prefix}/{dashboard_template}/compare/{comparison_entity}/{comparison_entity_id_or_query}"
    )
    response_model = AutomagicDashboardResponse


class AutomagicEntityCompareRequest(EndpointRequest[AutomagicDashboardResponse]):
    entity: str
    entity_id_or_query: str
    comparison_entity: str
    comparison_entity_id_or_query: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = (
        "/api/automagic-dashboards/{entity}/{entity_id_or_query}/compare/"
        "{comparison_entity}/{comparison_entity_id_or_query}"
    )
    response_model = AutomagicDashboardResponse


class AutomagicEntityQueryMetadataRequest(EndpointRequest[AutomagicDashboardResponse]):
    entity: str
    entity_id_or_query: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/automagic-dashboards/{entity}/{entity_id_or_query}/query_metadata"
    response_model = AutomagicDashboardResponse


class AutomagicEntityRuleRequest(EndpointRequest[AutomagicDashboardResponse]):
    entity: str
    entity_id_or_query: str
    prefix: str
    dashboard_template: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = (
        "/api/automagic-dashboards/{entity}/{entity_id_or_query}/rule/{prefix}/{dashboard_template}"
    )
    response_model = AutomagicDashboardResponse


class AutomagicEntityRuleCompareRequest(EndpointRequest[AutomagicDashboardResponse]):
    entity: str
    entity_id_or_query: str
    prefix: str
    dashboard_template: str
    comparison_entity: str
    comparison_entity_id_or_query: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = (
        "/api/automagic-dashboards/{entity}/{entity_id_or_query}/rule/{prefix}/{dashboard_template}/compare/"
        "{comparison_entity}/{comparison_entity_id_or_query}"
    )
    response_model = AutomagicDashboardResponse


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
