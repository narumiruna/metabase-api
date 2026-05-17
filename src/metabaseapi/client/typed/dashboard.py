from __future__ import annotations

from typing import TYPE_CHECKING

from metabaseapi.endpoints.entities import Dashboard
from metabaseapi.endpoints.requests.dashboard import CopyDashboardRequest
from metabaseapi.endpoints.requests.dashboard import CreateDashboardPublicLinkRequest
from metabaseapi.endpoints.requests.dashboard import DashboardParamRemappingRequest
from metabaseapi.endpoints.requests.dashboard import DashboardParamSearchRequest
from metabaseapi.endpoints.requests.dashboard import DashboardParamValuesRequest
from metabaseapi.endpoints.requests.dashboard import DeleteDashboardPublicLinkRequest
from metabaseapi.endpoints.requests.dashboard import DeleteDashboardRequest
from metabaseapi.endpoints.requests.dashboard import ExecuteDashboardDashcardRequest
from metabaseapi.endpoints.requests.dashboard import GetDashboardDashcardExecuteRequest
from metabaseapi.endpoints.requests.dashboard import GetDashboardEmbeddableRequest
from metabaseapi.endpoints.requests.dashboard import GetDashboardItemsRequest
from metabaseapi.endpoints.requests.dashboard import GetDashboardPublicRequest
from metabaseapi.endpoints.requests.dashboard import GetDashboardQueryMetadataRequest
from metabaseapi.endpoints.requests.dashboard import GetDashboardRelatedRequest
from metabaseapi.endpoints.requests.dashboard import GetDashboardRequest
from metabaseapi.endpoints.requests.dashboard import ListDashboardsRequest
from metabaseapi.endpoints.requests.dashboard import PostDashboardPivotQueryRequest
from metabaseapi.endpoints.requests.dashboard import PostDashboardRequest
from metabaseapi.endpoints.requests.dashboard import SaveDashboardRequest
from metabaseapi.endpoints.requests.dashboard import SaveDashboardToCollectionRequest
from metabaseapi.endpoints.requests.dashboard import UpdateDashboardCardsRequest
from metabaseapi.endpoints.requests.dashboard import UpdateDashboardRequest
from metabaseapi.endpoints.responses import GenericOperationResponse
from metabaseapi.endpoints.responses import ListDashboardsResponse
from metabaseapi.wire import QueryParamValue

if TYPE_CHECKING:
    from metabaseapi.client.http import MetabaseClient


async def create_dashboard_typed(client: MetabaseClient, body: dict[str, object]) -> Dashboard:
    return await client.run(PostDashboardRequest(body=dict(body)))


async def list_dashboards_typed(client: MetabaseClient) -> ListDashboardsResponse:
    return await client.run(ListDashboardsRequest())


async def get_dashboard_typed(client: MetabaseClient, dashboard_id: int | str) -> Dashboard:
    return await client.run(GetDashboardRequest(dashboard_id=dashboard_id))


async def get_dashboard_embeddable_typed(client: MetabaseClient) -> GenericOperationResponse:
    return await client.run(GetDashboardEmbeddableRequest())


async def get_dashboard_public_typed(client: MetabaseClient) -> GenericOperationResponse:
    return await client.run(GetDashboardPublicRequest())


async def query_dashboard_card_pivot_typed(
    client: MetabaseClient,
    dashboard_id: int | str,
    dashcard_id: int | str,
    card_id: int | str,
    body: dict[str, object] | None = None,
) -> GenericOperationResponse:
    return await client.run(
        PostDashboardPivotQueryRequest(
            dashboard_id=dashboard_id,
            dashcard_id=dashcard_id,
            card_id=card_id,
            body=body,
        )
    )


async def save_dashboard_typed(client: MetabaseClient, body: dict[str, object]) -> GenericOperationResponse:
    return await client.run(SaveDashboardRequest(body=body))


async def save_dashboard_to_collection_typed(
    client: MetabaseClient,
    parent_collection_id: int | str,
    body: dict[str, object],
) -> GenericOperationResponse:
    return await client.run(SaveDashboardToCollectionRequest(parent_collection_id=parent_collection_id, body=body))


async def get_dashboard_dashcard_execute_typed(
    client: MetabaseClient,
    dashboard_id: int | str,
    dashcard_id: int | str,
    *,
    parameters: dict[str, QueryParamValue] | None = None,
) -> GenericOperationResponse:
    return await client.run(
        GetDashboardDashcardExecuteRequest(
            dashboard_id=dashboard_id,
            dashcard_id=dashcard_id,
            parameters=parameters or {},
        )
    )


async def execute_dashboard_dashcard_typed(
    client: MetabaseClient,
    dashboard_id: int | str,
    dashcard_id: int | str,
    *,
    parameters: dict[str, object] | None = None,
) -> GenericOperationResponse:
    return await client.run(
        ExecuteDashboardDashcardRequest(
            dashboard_id=dashboard_id,
            dashcard_id=dashcard_id,
            parameters=parameters or {},
        )
    )


async def create_dashboard_public_link_typed(
    client: MetabaseClient, dashboard_id: int | str
) -> GenericOperationResponse:
    return await client.run(CreateDashboardPublicLinkRequest(dashboard_id=dashboard_id))


async def delete_dashboard_public_link_typed(
    client: MetabaseClient, dashboard_id: int | str
) -> GenericOperationResponse:
    return await client.run(DeleteDashboardPublicLinkRequest(dashboard_id=dashboard_id))


async def copy_dashboard_typed(
    client: MetabaseClient,
    from_dashboard_id: int | str,
    body: dict[str, object] | None = None,
) -> Dashboard:
    return await client.run(CopyDashboardRequest(from_dashboard_id=from_dashboard_id, body=body))


async def delete_dashboard_typed(client: MetabaseClient, dashboard_id: int | str) -> GenericOperationResponse:
    return await client.run(DeleteDashboardRequest(dashboard_id=dashboard_id))


async def update_dashboard_typed(client: MetabaseClient, dashboard_id: int | str, body: dict[str, object]) -> Dashboard:
    return await client.run(UpdateDashboardRequest(dashboard_id=dashboard_id, body=body))


async def update_dashboard_cards_typed(
    client: MetabaseClient,
    dashboard_id: int | str,
    body: dict[str, object],
) -> GenericOperationResponse:
    return await client.run(UpdateDashboardCardsRequest(dashboard_id=dashboard_id, body=body))


async def get_dashboard_items_typed(client: MetabaseClient, dashboard_id: int | str) -> GenericOperationResponse:
    return await client.run(GetDashboardItemsRequest(dashboard_id=dashboard_id))


async def get_dashboard_param_remapping_typed(
    client: MetabaseClient,
    dashboard_id: int | str,
    param_key: str,
    *,
    parameters: dict[str, QueryParamValue] | None = None,
) -> GenericOperationResponse:
    return await client.run(
        DashboardParamRemappingRequest(
            dashboard_id=dashboard_id,
            param_key=param_key,
            parameters=parameters or {},
        )
    )


async def get_dashboard_param_search_values_typed(
    client: MetabaseClient,
    dashboard_id: int | str,
    param_key: str,
    query: str,
    *,
    parameters: dict[str, QueryParamValue] | None = None,
) -> GenericOperationResponse:
    return await client.run(
        DashboardParamSearchRequest(
            dashboard_id=dashboard_id,
            param_key=param_key,
            query=query,
            parameters=parameters or {},
        )
    )


async def get_dashboard_param_values_typed(
    client: MetabaseClient,
    dashboard_id: int | str,
    param_key: str,
    *,
    parameters: dict[str, QueryParamValue] | None = None,
) -> GenericOperationResponse:
    return await client.run(
        DashboardParamValuesRequest(
            dashboard_id=dashboard_id,
            param_key=param_key,
            parameters=parameters or {},
        )
    )


async def get_dashboard_query_metadata_typed(
    client: MetabaseClient, dashboard_id: int | str
) -> GenericOperationResponse:
    return await client.run(GetDashboardQueryMetadataRequest(dashboard_id=dashboard_id))


async def get_dashboard_related_typed(client: MetabaseClient, dashboard_id: int | str) -> GenericOperationResponse:
    return await client.run(GetDashboardRelatedRequest(dashboard_id=dashboard_id))


__all__ = [
    "copy_dashboard_typed",
    "create_dashboard_public_link_typed",
    "create_dashboard_typed",
    "delete_dashboard_public_link_typed",
    "delete_dashboard_typed",
    "execute_dashboard_dashcard_typed",
    "get_dashboard_dashcard_execute_typed",
    "get_dashboard_embeddable_typed",
    "get_dashboard_items_typed",
    "get_dashboard_param_remapping_typed",
    "get_dashboard_param_search_values_typed",
    "get_dashboard_param_values_typed",
    "get_dashboard_public_typed",
    "get_dashboard_query_metadata_typed",
    "get_dashboard_related_typed",
    "get_dashboard_typed",
    "list_dashboards_typed",
    "query_dashboard_card_pivot_typed",
    "save_dashboard_to_collection_typed",
    "save_dashboard_typed",
    "update_dashboard_cards_typed",
    "update_dashboard_typed",
]
