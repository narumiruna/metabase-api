from __future__ import annotations

from collections.abc import Mapping
from typing import Protocol
from typing import TypeVar

import httpx

from metabaseapi.client.raw.activity import _MetabaseClientRawMixin as _MetabaseClientActivityRawMixin
from metabaseapi.client.raw.agent import _MetabaseClientRawMixin as _MetabaseClientAgentRawMixin
from metabaseapi.client.raw.alerts import _MetabaseClientRawMixin as _MetabaseClientAlertsRawMixin
from metabaseapi.client.raw.analytics import _MetabaseClientRawMixin as _MetabaseClientAnalyticsRawMixin
from metabaseapi.client.raw.api_key import _MetabaseClientRawMixin as _MetabaseClientApiKeyRawMixin
from metabaseapi.client.raw.automagic import _MetabaseClientRawMixin as _MetabaseClientAutomagicRawMixin
from metabaseapi.client.raw.bookmarks import _MetabaseClientRawMixin as _MetabaseClientBookmarksRawMixin
from metabaseapi.client.raw.bug_reporting import _MetabaseClientRawMixin as _MetabaseClientBugReportingRawMixin
from metabaseapi.client.raw.cache import _MetabaseClientRawMixin as _MetabaseClientCacheRawMixin
from metabaseapi.client.raw.channels import _MetabaseClientRawMixin as _MetabaseClientChannelsRawMixin
from metabaseapi.client.raw.cloud import _MetabaseClientRawMixin as _MetabaseClientCloudRawMixin
from metabaseapi.client.raw.collections import _MetabaseClientRawMixin as _MetabaseClientCollectionsRawMixin
from metabaseapi.client.raw.comments import _MetabaseClientRawMixin as _MetabaseClientCommentsRawMixin
from metabaseapi.client.raw.databases import _MetabaseClientRawMixin as _MetabaseClientDatabasesRawMixin
from metabaseapi.client.raw.tables import _MetabaseClientRawMixin as _MetabaseClientTablesRawMixin
from metabaseapi.client.raw.users import _MetabaseClientRawMixin as _MetabaseClientUsersRawMixin
from metabaseapi.client.typed.activity import _MetabaseClientTypedMixin as _MetabaseClientActivityTypedMixin
from metabaseapi.client.typed.agent import _MetabaseClientTypedMixin as _MetabaseClientAgentTypedMixin
from metabaseapi.client.typed.alerts import _MetabaseClientTypedMixin as _MetabaseClientAlertsTypedMixin
from metabaseapi.client.typed.analytics import _MetabaseClientTypedMixin as _MetabaseClientAnalyticsTypedMixin
from metabaseapi.client.typed.api_key import _MetabaseClientTypedMixin as _MetabaseClientApiKeyTypedMixin
from metabaseapi.client.typed.automagic import _MetabaseClientTypedMixin as _MetabaseClientAutomagicTypedMixin
from metabaseapi.client.typed.bookmarks import _MetabaseClientTypedMixin as _MetabaseClientBookmarksTypedMixin
from metabaseapi.client.typed.bug_reporting import _MetabaseClientTypedMixin as _MetabaseClientBugReportingTypedMixin
from metabaseapi.client.typed.cache import _MetabaseClientTypedMixin as _MetabaseClientCacheTypedMixin
from metabaseapi.client.typed.channels import _MetabaseClientTypedMixin as _MetabaseClientChannelsTypedMixin
from metabaseapi.client.typed.cloud import _MetabaseClientTypedMixin as _MetabaseClientCloudTypedMixin
from metabaseapi.client.typed.collections import _MetabaseClientTypedMixin as _MetabaseClientCollectionsTypedMixin
from metabaseapi.client.typed.comments import _MetabaseClientTypedMixin as _MetabaseClientCommentsTypedMixin
from metabaseapi.client.typed.databases import _MetabaseClientTypedMixin as _MetabaseClientDatabasesTypedMixin
from metabaseapi.client.typed.tables import _MetabaseClientTypedMixin as _MetabaseClientTablesTypedMixin
from metabaseapi.client.typed.users import _MetabaseClientTypedMixin as _MetabaseClientUsersTypedMixin
from metabaseapi.errors import MetabaseDecodeError
from metabaseapi.errors import MetabaseHTTPStatusError
from metabaseapi.errors import MetabaseNetworkError
from metabaseapi.metabase import Card
from metabaseapi.metabase import CardParamsSearchRequest
from metabaseapi.metabase import CardParamsValuesRequest
from metabaseapi.metabase import CardQueryExportRequest
from metabaseapi.metabase import CardQueryRequest
from metabaseapi.metabase import CardRemappingRequest
from metabaseapi.metabase import CardsDashboardsRequest
from metabaseapi.metabase import CardsDashboardsResponse
from metabaseapi.metabase import CopyCardRequest
from metabaseapi.metabase import CopyDashboardRequest
from metabaseapi.metabase import CreateCardPublicLinkRequest
from metabaseapi.metabase import CreateCardRequest
from metabaseapi.metabase import CreateDashboardPublicLinkRequest
from metabaseapi.metabase import Dashboard
from metabaseapi.metabase import DashboardParamRemappingRequest
from metabaseapi.metabase import DashboardParamSearchRequest
from metabaseapi.metabase import DashboardParamValuesRequest
from metabaseapi.metabase import DataStudioTableDiscardValuesRequest
from metabaseapi.metabase import DataStudioTableEditRequest
from metabaseapi.metabase import DataStudioTableRescanValuesRequest
from metabaseapi.metabase import DataStudioTableSelectionRequest
from metabaseapi.metabase import DataStudioTableSyncSchemaRequest
from metabaseapi.metabase import DeleteCardPublicLinkRequest
from metabaseapi.metabase import DeleteCardRequest
from metabaseapi.metabase import DeleteDashboardPublicLinkRequest
from metabaseapi.metabase import DeleteDashboardRequest
from metabaseapi.metabase import ExecuteDashboardDashcardRequest
from metabaseapi.metabase import GenericOperationResponse
from metabaseapi.metabase import GetCardCollectionsRequest
from metabaseapi.metabase import GetCardDashboardsRequest
from metabaseapi.metabase import GetCardEmbeddableRequest
from metabaseapi.metabase import GetCardPublicRequest
from metabaseapi.metabase import GetCardQueryMetadataRequest
from metabaseapi.metabase import GetCardRequest
from metabaseapi.metabase import GetCardSeriesRequest
from metabaseapi.metabase import GetDashboardDashcardExecuteRequest
from metabaseapi.metabase import GetDashboardEmbeddableRequest
from metabaseapi.metabase import GetDashboardItemsRequest
from metabaseapi.metabase import GetDashboardPublicRequest
from metabaseapi.metabase import GetDashboardQueryMetadataRequest
from metabaseapi.metabase import GetDashboardRelatedRequest
from metabaseapi.metabase import GetDashboardRequest
from metabaseapi.metabase import ListCardsRequest
from metabaseapi.metabase import ListCardsResponse
from metabaseapi.metabase import ListDashboardsRequest
from metabaseapi.metabase import ListDashboardsResponse
from metabaseapi.metabase import MoveCardsRequest
from metabaseapi.metabase import PostCardPivotQueryRequest
from metabaseapi.metabase import PostDashboardPivotQueryRequest
from metabaseapi.metabase import PostDashboardRequest
from metabaseapi.metabase import SaveDashboardRequest
from metabaseapi.metabase import SaveDashboardToCollectionRequest
from metabaseapi.metabase import UpdateCardRequest
from metabaseapi.metabase import UpdateDashboardCardsRequest
from metabaseapi.metabase import UpdateDashboardRequest
from metabaseapi.models import APIRequestModel
from metabaseapi.models import APIResponseModel
from metabaseapi.models import JSONValue
from metabaseapi.models import QueryParamPrimitive
from metabaseapi.models import QueryParamValue
from metabaseapi.settings import Settings


class _MetabaseClientRawMixin(
    _MetabaseClientUsersRawMixin,
    _MetabaseClientAnalyticsRawMixin,
    _MetabaseClientAlertsRawMixin,
    _MetabaseClientApiKeyRawMixin,
    _MetabaseClientAgentRawMixin,
    _MetabaseClientActivityRawMixin,
    _MetabaseClientBookmarksRawMixin,
    _MetabaseClientCacheRawMixin,
    _MetabaseClientCollectionsRawMixin,
    _MetabaseClientChannelsRawMixin,
    _MetabaseClientCloudRawMixin,
    _MetabaseClientDatabasesRawMixin,
    _MetabaseClientAutomagicRawMixin,
    _MetabaseClientCommentsRawMixin,
    _MetabaseClientBugReportingRawMixin,
    _MetabaseClientTablesRawMixin,
):
    """Resource-scoped raw mixin."""


class _MetabaseClientTypedMixin(
    _MetabaseClientRawMixin,
    _MetabaseClientUsersTypedMixin,
    _MetabaseClientAnalyticsTypedMixin,
    _MetabaseClientAlertsTypedMixin,
    _MetabaseClientApiKeyTypedMixin,
    _MetabaseClientAgentTypedMixin,
    _MetabaseClientBookmarksTypedMixin,
    _MetabaseClientCacheTypedMixin,
    _MetabaseClientCollectionsTypedMixin,
    _MetabaseClientChannelsTypedMixin,
    _MetabaseClientCloudTypedMixin,
    _MetabaseClientDatabasesTypedMixin,
    _MetabaseClientAutomagicTypedMixin,
    _MetabaseClientCommentsTypedMixin,
    _MetabaseClientBugReportingTypedMixin,
    _MetabaseClientTablesTypedMixin,
    _MetabaseClientActivityTypedMixin,
):
    """Resource-scoped typed mixin."""


class _ExecutableRequest[ResponseT](Protocol):
    async def do(self, client: MetabaseClient) -> ResponseT: ...


ResponseT = TypeVar("ResponseT")


class MetabaseClient(_MetabaseClientTypedMixin):
    """Async Metabase API client with a small convenience API surface."""

    def __init__(
        self,
        base_url: str,
        api_key: str,
        timeout_seconds: float = 30.0,
        verify_ssl: bool = True,
        client: httpx.AsyncClient | None = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self.api_key = api_key
        self.timeout_seconds = timeout_seconds
        self.verify_ssl = verify_ssl
        self._provided_client = client
        self._client = client or httpx.AsyncClient(
            timeout=httpx.Timeout(timeout=timeout_seconds),
            verify=verify_ssl,
        )

    @classmethod
    def from_settings(cls, settings: Settings, client: httpx.AsyncClient | None = None) -> MetabaseClient:
        api_key = settings.requires_api_key()
        return cls(
            base_url=settings.base_url,
            api_key=api_key,
            timeout_seconds=settings.timeout_seconds,
            verify_ssl=settings.verify_ssl,
            client=client,
        )

    async def __aenter__(self) -> MetabaseClient:
        return self

    async def __aexit__(
        self,
        _exc_type: type[BaseException] | None,
        _exc_value: BaseException | None,
        _traceback: object | None,
    ) -> None:
        await self.close()

    async def close(self) -> None:
        if self._provided_client is None:
            await self._client.aclose()

    def _request_url(self, path: str) -> str:
        normalized = path.strip()
        if not normalized.startswith("http://") and not normalized.startswith("https://"):
            normalized = f"/{normalized.lstrip('/')}"
            return f"{self.base_url}{normalized}"
        return normalized

    async def request(
        self,
        method: str,
        path: str,
        *,
        params: Mapping[str, QueryParamValue] | None = None,
        json_data: JSONValue | None = None,
    ) -> JSONValue | None:
        request_model = APIRequestModel(
            method=method,
            path=path,
            params=dict(params or {}),
            body=json_data,
        )

        url = self._request_url(request_model.path)
        headers = {"X-API-Key": self.api_key, "Accept": "application/json"}
        try:
            match request_model.method:
                case "GET":
                    response = await self._client.get(url, params=request_model.params, headers=headers)
                case "POST":
                    response = await self._client.post(
                        url,
                        params=request_model.params,
                        json=request_model.body,
                        headers=headers,
                    )
                case "PUT":
                    response = await self._client.put(
                        url,
                        params=request_model.params,
                        json=request_model.body,
                        headers=headers,
                    )
                case "PATCH":
                    response = await self._client.patch(
                        url,
                        params=request_model.params,
                        json=request_model.body,
                        headers=headers,
                    )
                case "DELETE":
                    if request_model.body is None:
                        response = await self._client.delete(url, params=request_model.params, headers=headers)
                    else:
                        # httpx.AsyncClient.delete() has no JSON-body parameter, but Metabase documents
                        # DELETE /api/cache with a JSON body.
                        response = await self._client.request(
                            "DELETE",
                            url,
                            params=request_model.params,
                            json=request_model.body,
                            headers=headers,
                        )
                case _:
                    raise AssertionError("unsupported HTTP method after request validation")
        except httpx.TimeoutException as exc:
            raise MetabaseNetworkError("Metabase request timed out") from exc
        except httpx.NetworkError as exc:
            raise MetabaseNetworkError("Metabase network error") from exc

        payload = self._decode_response_payload(response)
        response_model = APIResponseModel(
            status_code=response.status_code,
            payload=payload,
            content_type=response.headers.get("content-type", None),
        )

        if response.status_code < 200 or response.status_code >= 300:
            raise MetabaseHTTPStatusError(response.status_code, response_model.payload)

        return response_model.payload

    def _decode_response_payload(self, response: httpx.Response) -> JSONValue | None:

        if response.status_code == 204 or not response.content:
            return None

        content_type = response.headers.get("content-type", "").lower()
        if "application/json" in content_type or response.text.strip().startswith(("{", "[")):
            try:
                return response.json()
            except ValueError as exc:
                raise MetabaseDecodeError("Invalid JSON in response") from exc

        return {
            "content_type": content_type or None,
            "text": response.text,
        }

    async def get(
        self,
        path: str,
        *,
        params: Mapping[str, QueryParamValue] | None = None,
    ) -> JSONValue | None:
        return await self.request("GET", path, params=params)

    async def post(
        self,
        path: str,
        *,
        params: Mapping[str, QueryParamValue] | None = None,
        body: JSONValue | None = None,
    ) -> JSONValue | None:
        return await self.request("POST", path, params=params, json_data=body)

    async def put(
        self,
        path: str,
        *,
        params: Mapping[str, QueryParamValue] | None = None,
        body: JSONValue | None = None,
    ) -> JSONValue | None:
        return await self.request("PUT", path, params=params, json_data=body)

    async def patch(
        self,
        path: str,
        *,
        params: Mapping[str, QueryParamValue] | None = None,
        body: JSONValue | None = None,
    ) -> JSONValue | None:
        return await self.request("PATCH", path, params=params, json_data=body)

    async def delete(
        self,
        path: str,
        *,
        params: Mapping[str, QueryParamValue] | None = None,
        body: JSONValue | None = None,
    ) -> JSONValue | None:
        return await self.request("DELETE", path, params=params, json_data=body)

    # action, automagic, agent, and database methods are now moved into dedicated mixins.

    async def list_cards(self) -> JSONValue | None:
        return await self.get("/api/card")

    async def create_card(
        self,
        *,
        name: str,
        dataset_query: Mapping[str, object],
        display: str,
        visualization_settings: Mapping[str, object] | None = None,
        card_type: str | None = "question",
        collection_id: int | str | None = None,
        description: str | None = None,
        parameters: list[object] | None = None,
        result_metadata: list[object] | None = None,
    ) -> JSONValue | None:
        body: dict[str, object] = {
            "name": name,
            "dataset_query": dict(dataset_query),
            "display": display,
            "visualization_settings": dict(visualization_settings or {}),
        }
        if card_type is not None:
            body["type"] = card_type
        if collection_id is not None:
            body["collection_id"] = collection_id
        if description is not None:
            body["description"] = description
        if parameters is not None:
            body["parameters"] = parameters
        if result_metadata is not None:
            body["result_metadata"] = result_metadata
        return await self.post("/api/card", body=body)

    async def create_question(
        self,
        *,
        name: str,
        dataset_query: Mapping[str, object],
        display: str,
        visualization_settings: Mapping[str, object] | None = None,
        collection_id: int | str | None = None,
        description: str | None = None,
        parameters: list[object] | None = None,
        result_metadata: list[object] | None = None,
    ) -> JSONValue | None:
        return await self.create_card(
            name=name,
            dataset_query=dataset_query,
            display=display,
            visualization_settings=visualization_settings,
            card_type="question",
            collection_id=collection_id,
            description=description,
            parameters=parameters,
            result_metadata=result_metadata,
        )

    async def card_collections(
        self,
        card_ids: list[int | str],
        collection_id: int | str | None = None,
    ) -> JSONValue | None:
        body: dict[str, object] = {"card_ids": card_ids}
        if collection_id is not None:
            body["collection_id"] = collection_id
        return await self.post("/api/card/collections", body=body)

    async def list_embeddable_cards(self) -> JSONValue | None:
        return await self.get("/api/card/embeddable")

    async def pivot_query(
        self,
        card_id: int | str,
        body: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        return await self.post(
            f"/api/card/pivot/{card_id}/query",
            body=dict(body) if body is not None else None,
        )

    async def list_public_cards(self) -> JSONValue | None:
        return await self.get("/api/card/public")

    async def get_card_param_search_values(self, card_id: int | str, param_key: str, query: str) -> JSONValue | None:
        return await self.get(f"/api/card/{card_id}/params/{param_key}/search/{query}")

    async def get_card_param_values(self, card_id: int | str, param_key: str) -> JSONValue | None:
        return await self.get(f"/api/card/{card_id}/params/{param_key}/values")

    async def create_card_public_link(self, card_id: int | str) -> JSONValue | None:
        return await self.post(f"/api/card/{card_id}/public_link")

    async def delete_card_public_link(self, card_id: int | str) -> JSONValue | None:
        return await self.delete(f"/api/card/{card_id}/public_link")

    async def query_card(
        self,
        card_id: int | str,
        body: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        return await self.post(
            f"/api/card/{card_id}/query",
            body=dict(body) if body is not None else None,
        )

    async def query_card_export(
        self,
        card_id: int | str,
        export_format: str,
        body: Mapping[str, object] | None = None,
        *,
        pivot_results: bool | None = None,
        format_rows: bool | None = None,
    ) -> JSONValue | None:
        params: dict[str, QueryParamValue] = {}
        if pivot_results is not None:
            params["pivot-results"] = pivot_results
        if format_rows is not None:
            params["format-rows"] = format_rows
        return await self.post(
            f"/api/card/{card_id}/query/{export_format}",
            body=dict(body) if body is not None else None,
            params=params or None,
        )

    async def update_card(self, card_id: int | str, body: Mapping[str, object]) -> JSONValue | None:
        return await self.put(f"/api/card/{card_id}", body=dict(body))

    async def delete_card(self, card_id: int | str) -> JSONValue | None:
        return await self.delete(f"/api/card/{card_id}")

    async def copy_card(self, card_id: int | str) -> JSONValue | None:
        return await self.post(f"/api/card/{card_id}/copy")

    async def cards_dashboards(self, card_ids: list[int | str]) -> JSONValue | None:
        return await self.post("/api/cards/dashboards", body={"card_ids": card_ids})

    async def move_cards(self, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/cards/move", body=dict(body))

    async def get_card_dashboards(self, card_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/card/{card_id}/dashboards")

    async def get_card_param_remapping(self, card_id: int | str, param_key: str) -> JSONValue | None:
        return await self.get(f"/api/card/{card_id}/params/{param_key}/remapping")

    async def get_card_query_metadata(self, card_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/card/{card_id}/query_metadata")

    async def get_card_series(self, card_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/card/{card_id}/series")

    async def get_card(self, card_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/card/{card_id}")

    async def create_dashboard(self, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/dashboard", body=dict(body))

    async def list_dashboards(self) -> JSONValue | None:
        return await self.get("/api/dashboard")

    async def get_dashboard(self, dashboard_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/dashboard/{dashboard_id}")

    async def get_dashboard_embeddable(self) -> JSONValue | None:
        return await self.get("/api/dashboard/embeddable")

    async def get_dashboard_public(self) -> JSONValue | None:
        return await self.get("/api/dashboard/public")

    async def get_dashboard_params_valid_filter_fields(
        self,
        *,
        filtered: list[int | str] | None = None,
        filtering: list[int | str] | None = None,
    ) -> JSONValue | None:
        params: dict[str, QueryParamValue] = {}
        if filtered is not None:
            filtered_values: list[QueryParamPrimitive] = list(filtered)
            params["filtered"] = filtered_values
        if filtering is not None:
            filtering_values: list[QueryParamPrimitive] = list(filtering)
            params["filtering"] = filtering_values
        return await self.get("/api/dashboard/params/valid-filter-fields", params=params or None)

    async def query_dashboard_card(
        self,
        dashboard_id: int | str,
        dashcard_id: int | str,
        card_id: int | str,
        body: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        payload = dict(body) if body is not None else None
        return await self.post(
            f"/api/dashboard/{dashboard_id}/dashcard/{dashcard_id}/card/{card_id}/query",
            body=payload,
        )

    async def query_dashboard_card_export(
        self,
        dashboard_id: int | str,
        dashcard_id: int | str,
        card_id: int | str,
        export_format: str,
        body: Mapping[str, object] | None = None,
        *,
        pivot_results: bool | None = None,
        format_rows: bool | None = None,
    ) -> JSONValue | None:
        payload = dict(body) if body is not None else None
        params: dict[str, QueryParamValue] = {}
        if pivot_results is not None:
            params["pivot-results"] = pivot_results
        if format_rows is not None:
            params["format-rows"] = format_rows
        return await self.post(
            f"/api/dashboard/{dashboard_id}/dashcard/{dashcard_id}/card/{card_id}/query/{export_format}",
            body=payload,
            params=params or None,
        )

    async def query_dashboard_card_pivot(
        self,
        dashboard_id: int | str,
        dashcard_id: int | str,
        card_id: int | str,
        body: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        payload = dict(body) if body is not None else None
        return await self.post(
            f"/api/dashboard/pivot/{dashboard_id}/dashcard/{dashcard_id}/card/{card_id}/query",
            body=payload,
        )

    async def save_dashboard(self, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/dashboard/save", body=dict(body))

    async def save_dashboard_to_collection(
        self,
        parent_collection_id: int | str,
        body: Mapping[str, object],
    ) -> JSONValue | None:
        return await self.post(f"/api/dashboard/save/collection/{parent_collection_id}", body=dict(body))

    async def get_dashboard_dashcard_execute(
        self,
        dashboard_id: int | str,
        dashcard_id: int | str,
        *,
        parameters: Mapping[str, QueryParamValue] | None = None,
    ) -> JSONValue | None:
        return await self.get(
            f"/api/dashboard/{dashboard_id}/dashcard/{dashcard_id}/execute",
            params=parameters,
        )

    async def execute_dashboard_dashcard(
        self,
        dashboard_id: int | str,
        dashcard_id: int | str,
        *,
        parameters: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        return await self.post(
            f"/api/dashboard/{dashboard_id}/dashcard/{dashcard_id}/execute",
            body={"parameters": dict(parameters or {})},
        )

    async def create_dashboard_public_link(self, dashboard_id: int | str) -> JSONValue | None:
        return await self.post(f"/api/dashboard/{dashboard_id}/public_link")

    async def delete_dashboard_public_link(self, dashboard_id: int | str) -> JSONValue | None:
        return await self.delete(f"/api/dashboard/{dashboard_id}/public_link")

    async def copy_dashboard(
        self,
        from_dashboard_id: int | str,
        body: Mapping[str, object] | None = None,
    ) -> JSONValue | None:
        return await self.post(
            f"/api/dashboard/{from_dashboard_id}/copy",
            body=dict(body) if body is not None else None,
        )

    async def delete_dashboard(self, dashboard_id: int | str) -> JSONValue | None:
        return await self.delete(f"/api/dashboard/{dashboard_id}")

    async def update_dashboard(self, dashboard_id: int | str, body: Mapping[str, object]) -> JSONValue | None:
        return await self.put(f"/api/dashboard/{dashboard_id}", body=dict(body))

    async def update_dashboard_cards(self, dashboard_id: int | str, body: Mapping[str, object]) -> JSONValue | None:
        return await self.put(f"/api/dashboard/{dashboard_id}/cards", body=dict(body))

    async def get_dashboard_items(self, dashboard_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/dashboard/{dashboard_id}/items")

    async def get_dashboard_param_remapping(
        self,
        dashboard_id: int | str,
        param_key: str,
        *,
        parameters: Mapping[str, QueryParamValue] | None = None,
    ) -> JSONValue | None:
        return await self.get(
            f"/api/dashboard/{dashboard_id}/params/{param_key}/remapping",
            params=parameters,
        )

    async def get_dashboard_param_search_values(
        self,
        dashboard_id: int | str,
        param_key: str,
        query: str,
        *,
        parameters: Mapping[str, QueryParamValue] | None = None,
    ) -> JSONValue | None:
        return await self.get(
            f"/api/dashboard/{dashboard_id}/params/{param_key}/search/{query}",
            params=parameters,
        )

    async def get_dashboard_param_values(
        self,
        dashboard_id: int | str,
        param_key: str,
        *,
        parameters: Mapping[str, QueryParamValue] | None = None,
    ) -> JSONValue | None:
        return await self.get(
            f"/api/dashboard/{dashboard_id}/params/{param_key}/values",
            params=parameters,
        )

    async def get_dashboard_query_metadata(self, dashboard_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/dashboard/{dashboard_id}/query_metadata")

    async def get_dashboard_related(self, dashboard_id: int | str) -> JSONValue | None:
        return await self.get(f"/api/dashboard/{dashboard_id}/related")

    async def data_studio_table_discard_values(self, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/data-studio/table/discard-values", body=dict(body))

    async def data_studio_table_edit(self, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/data-studio/table/edit", body=dict(body))

    async def data_studio_table_rescan_values(self, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/data-studio/table/rescan-values", body=dict(body))

    async def data_studio_table_selection(self, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/data-studio/table/selection", body=dict(body))

    async def data_studio_table_sync_schema(self, body: Mapping[str, object]) -> JSONValue | None:
        return await self.post("/api/data-studio/table/sync-schema", body=dict(body))

    async def run[ResponseT](self, request_model: _ExecutableRequest[ResponseT]) -> ResponseT:
        return await request_model.do(self)

    # action, automagic, agent, and database typed methods are now moved into dedicated mixins.

    async def list_cards_typed(self) -> ListCardsResponse:
        return await self.run(ListCardsRequest())

    async def list_dashboards_typed(self) -> ListDashboardsResponse:
        return await self.run(ListDashboardsRequest())

    async def create_dashboard_typed(self, body: dict[str, object]) -> Dashboard:
        return await self.run(PostDashboardRequest(body=dict(body)))

    async def create_card_typed(
        self,
        *,
        name: str,
        dataset_query: dict[str, object],
        display: str,
        visualization_settings: dict[str, object] | None = None,
        card_type: str | None = "question",
        collection_id: int | str | None = None,
        description: str | None = None,
        parameters: list[object] | None = None,
        result_metadata: list[object] | None = None,
    ) -> Card:
        request = CreateCardRequest(
            name=name,
            dataset_query=dataset_query,
            display=display,
            visualization_settings=visualization_settings or {},
            type=card_type,
            collection_id=collection_id,
            description=description,
            parameters=parameters,
            result_metadata=result_metadata,
        )
        return await self.run(request)

    async def create_question_typed(
        self,
        *,
        name: str,
        dataset_query: dict[str, object],
        display: str,
        visualization_settings: dict[str, object] | None = None,
        collection_id: int | str | None = None,
        description: str | None = None,
        parameters: list[object] | None = None,
        result_metadata: list[object] | None = None,
    ) -> Card:
        return await self.create_card_typed(
            name=name,
            dataset_query=dataset_query,
            display=display,
            visualization_settings=visualization_settings,
            card_type="question",
            collection_id=collection_id,
            description=description,
            parameters=parameters,
            result_metadata=result_metadata,
        )

    async def get_card_typed(self, card_id: int | str) -> Card:
        return await self.run(GetCardRequest(card_id=card_id))

    async def get_card_collections_typed(
        self,
        card_ids: list[int | str],
        collection_id: int | str | None = None,
    ) -> GenericOperationResponse:
        return await self.run(GetCardCollectionsRequest(card_ids=card_ids, collection_id=collection_id))

    async def list_card_embeddable_typed(self) -> GenericOperationResponse:
        return await self.run(GetCardEmbeddableRequest())

    async def pivot_card_query_typed(
        self,
        card_id: int | str,
        body: dict[str, object] | None = None,
    ) -> GenericOperationResponse:
        return await self.run(PostCardPivotQueryRequest(card_id=card_id, body=body or {}))

    async def list_public_cards_typed(self) -> GenericOperationResponse:
        return await self.run(GetCardPublicRequest())

    async def get_card_param_search_values_typed(
        self,
        card_id: int | str,
        param_key: str,
        query: str,
    ) -> GenericOperationResponse:
        return await self.run(CardParamsSearchRequest(card_id=card_id, param_key=param_key, query=query))

    async def get_card_param_values_typed(self, card_id: int | str, param_key: str) -> GenericOperationResponse:
        return await self.run(CardParamsValuesRequest(card_id=card_id, param_key=param_key))

    async def create_card_public_link_typed(self, card_id: int | str) -> GenericOperationResponse:
        return await self.run(CreateCardPublicLinkRequest(card_id=card_id))

    async def delete_card_public_link_typed(self, card_id: int | str) -> GenericOperationResponse:
        return await self.run(DeleteCardPublicLinkRequest(card_id=card_id))

    async def query_card_typed(
        self,
        card_id: int | str,
        body: dict[str, object] | None = None,
    ) -> GenericOperationResponse:
        return await self.run(CardQueryRequest(card_id=card_id, body=body or {}))

    async def query_card_export_typed(
        self,
        card_id: int | str,
        export_format: str,
        body: dict[str, object] | None = None,
        *,
        pivot_results: bool | None = None,
        format_rows: bool | None = None,
    ) -> GenericOperationResponse:
        return await self.run(
            CardQueryExportRequest(
                card_id=card_id,
                export_format=export_format,
                body=body or {},
                pivot_results=pivot_results,
                format_rows=format_rows,
            )
        )

    async def cards_dashboards_typed(self, card_ids: list[int | str]) -> CardsDashboardsResponse:
        return await self.run(CardsDashboardsRequest(card_ids=card_ids))

    async def move_cards_typed(self, body: Mapping[str, object]) -> GenericOperationResponse:
        return await self.run(MoveCardsRequest(body=dict(body)))

    async def update_card_typed(self, card_id: int | str, body: dict[str, object]) -> Card:
        return await self.run(UpdateCardRequest(card_id=card_id, body=body))

    async def delete_card_typed(self, card_id: int | str) -> GenericOperationResponse:
        return await self.run(DeleteCardRequest(card_id=card_id))

    async def copy_card_typed(self, card_id: int | str, body: dict[str, object] | None = None) -> Card:
        return await self.run(CopyCardRequest(card_id=card_id, body=body or {}))

    async def get_card_dashboards_typed(self, card_id: int | str) -> GenericOperationResponse:
        return await self.run(GetCardDashboardsRequest(card_id=card_id))

    async def get_card_param_remapping_typed(
        self,
        card_id: int | str,
        param_key: str,
    ) -> GenericOperationResponse:
        return await self.run(CardRemappingRequest(card_id=card_id, param_key=param_key))

    async def get_card_query_metadata_typed(self, card_id: int | str) -> GenericOperationResponse:
        return await self.run(GetCardQueryMetadataRequest(card_id=card_id))

    async def get_card_series_typed(self, card_id: int | str) -> GenericOperationResponse:
        return await self.run(GetCardSeriesRequest(card_id=card_id))

    async def get_dashboard_typed(self, dashboard_id: int | str) -> Dashboard:
        return await self.run(GetDashboardRequest(dashboard_id=dashboard_id))

    async def get_dashboard_embeddable_typed(self) -> GenericOperationResponse:
        return await self.run(GetDashboardEmbeddableRequest())

    async def get_dashboard_public_typed(self) -> GenericOperationResponse:
        return await self.run(GetDashboardPublicRequest())

    async def query_dashboard_card_pivot_typed(
        self,
        dashboard_id: int | str,
        dashcard_id: int | str,
        card_id: int | str,
        body: dict[str, object] | None = None,
    ) -> GenericOperationResponse:
        return await self.run(
            PostDashboardPivotQueryRequest(
                dashboard_id=dashboard_id,
                dashcard_id=dashcard_id,
                card_id=card_id,
                body=body,
            )
        )

    async def save_dashboard_typed(self, body: dict[str, object]) -> GenericOperationResponse:
        return await self.run(SaveDashboardRequest(body=body))

    async def save_dashboard_to_collection_typed(
        self,
        parent_collection_id: int | str,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await self.run(SaveDashboardToCollectionRequest(parent_collection_id=parent_collection_id, body=body))

    async def get_dashboard_dashcard_execute_typed(
        self,
        dashboard_id: int | str,
        dashcard_id: int | str,
        *,
        parameters: dict[str, QueryParamValue] | None = None,
    ) -> GenericOperationResponse:
        return await self.run(
            GetDashboardDashcardExecuteRequest(
                dashboard_id=dashboard_id,
                dashcard_id=dashcard_id,
                parameters=parameters or {},
            )
        )

    async def execute_dashboard_dashcard_typed(
        self,
        dashboard_id: int | str,
        dashcard_id: int | str,
        *,
        parameters: dict[str, object] | None = None,
    ) -> GenericOperationResponse:
        return await self.run(
            ExecuteDashboardDashcardRequest(
                dashboard_id=dashboard_id,
                dashcard_id=dashcard_id,
                parameters=parameters or {},
            )
        )

    async def create_dashboard_public_link_typed(self, dashboard_id: int | str) -> GenericOperationResponse:
        return await self.run(CreateDashboardPublicLinkRequest(dashboard_id=dashboard_id))

    async def delete_dashboard_public_link_typed(self, dashboard_id: int | str) -> GenericOperationResponse:
        return await self.run(DeleteDashboardPublicLinkRequest(dashboard_id=dashboard_id))

    async def copy_dashboard_typed(
        self,
        from_dashboard_id: int | str,
        body: dict[str, object] | None = None,
    ) -> Dashboard:
        return await self.run(CopyDashboardRequest(from_dashboard_id=from_dashboard_id, body=body))

    async def delete_dashboard_typed(self, dashboard_id: int | str) -> GenericOperationResponse:
        return await self.run(DeleteDashboardRequest(dashboard_id=dashboard_id))

    async def update_dashboard_typed(self, dashboard_id: int | str, body: dict[str, object]) -> Dashboard:
        return await self.run(UpdateDashboardRequest(dashboard_id=dashboard_id, body=body))

    async def update_dashboard_cards_typed(
        self,
        dashboard_id: int | str,
        body: dict[str, object],
    ) -> GenericOperationResponse:
        return await self.run(UpdateDashboardCardsRequest(dashboard_id=dashboard_id, body=body))

    async def get_dashboard_items_typed(self, dashboard_id: int | str) -> GenericOperationResponse:
        return await self.run(GetDashboardItemsRequest(dashboard_id=dashboard_id))

    async def get_dashboard_param_remapping_typed(
        self,
        dashboard_id: int | str,
        param_key: str,
        *,
        parameters: dict[str, QueryParamValue] | None = None,
    ) -> GenericOperationResponse:
        return await self.run(
            DashboardParamRemappingRequest(
                dashboard_id=dashboard_id,
                param_key=param_key,
                parameters=parameters or {},
            )
        )

    async def get_dashboard_param_search_values_typed(
        self,
        dashboard_id: int | str,
        param_key: str,
        query: str,
        *,
        parameters: dict[str, QueryParamValue] | None = None,
    ) -> GenericOperationResponse:
        return await self.run(
            DashboardParamSearchRequest(
                dashboard_id=dashboard_id,
                param_key=param_key,
                query=query,
                parameters=parameters or {},
            )
        )

    async def get_dashboard_param_values_typed(
        self,
        dashboard_id: int | str,
        param_key: str,
        *,
        parameters: dict[str, QueryParamValue] | None = None,
    ) -> GenericOperationResponse:
        return await self.run(
            DashboardParamValuesRequest(
                dashboard_id=dashboard_id,
                param_key=param_key,
                parameters=parameters or {},
            )
        )

    async def get_dashboard_query_metadata_typed(self, dashboard_id: int | str) -> GenericOperationResponse:
        return await self.run(GetDashboardQueryMetadataRequest(dashboard_id=dashboard_id))

    async def get_dashboard_related_typed(self, dashboard_id: int | str) -> GenericOperationResponse:
        return await self.run(GetDashboardRelatedRequest(dashboard_id=dashboard_id))

    async def data_studio_table_discard_values_typed(self, body: dict[str, object]) -> GenericOperationResponse:
        return await self.run(DataStudioTableDiscardValuesRequest(body=body))

    async def data_studio_table_edit_typed(self, body: dict[str, object]) -> GenericOperationResponse:
        return await self.run(DataStudioTableEditRequest(body=body))

    async def data_studio_table_rescan_values_typed(self, body: dict[str, object]) -> GenericOperationResponse:
        return await self.run(DataStudioTableRescanValuesRequest(body=body))

    async def data_studio_table_selection_typed(self, body: dict[str, object]) -> GenericOperationResponse:
        return await self.run(DataStudioTableSelectionRequest(body=body))

    async def data_studio_table_sync_schema_typed(self, body: dict[str, object]) -> GenericOperationResponse:
        return await self.run(DataStudioTableSyncSchemaRequest(body=body))
