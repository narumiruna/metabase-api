from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.execution import MetabaseRequestClient
from metabaseapi.endpoints.responses.common import GenericOperationResponse


class AutomagicDashboardRequest(EndpointRequest[GenericOperationResponse]):
    path: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/automagic-dashboards/{path}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/automagic-dashboards/{self.path.lstrip('/')}"


class AutomagicDatabaseCandidatesRequest(EndpointRequest[GenericOperationResponse]):
    database_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/automagic-dashboards/database/{id}/candidates"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/automagic-dashboards/database/{self.database_id}/candidates"


class AutomagicModelIndexPrimaryKeyRequest(EndpointRequest[GenericOperationResponse]):
    model_index_id: int | str
    primary_key_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/automagic-dashboards/model_index/{model-index-id}/primary_key/{pk-id}"

    async def do(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return await self.execute(client, GenericOperationResponse)

    def do_sync(self, client: MetabaseRequestClient) -> GenericOperationResponse:
        return self.execute_sync(client, GenericOperationResponse)

    def resolve_path(self) -> str:
        return f"/api/automagic-dashboards/model_index/{self.model_index_id}/primary_key/{self.primary_key_id}"
