from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.tiles import AdHocQueryTileResponse
from metabaseapi.endpoints.responses.tiles import DashboardCardTileResponse
from metabaseapi.endpoints.responses.tiles import SavedCardTileResponse
from metabaseapi.wire import QueryParamValue


class GetSavedCardTileRequest(EndpointRequest[SavedCardTileResponse]):
    card_id: int | str
    zoom: int
    x: int
    y: int
    lat_field: str
    lon_field: str
    parameters: str | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/tiles/{card_id}/{zoom}/{x}/{y}"
    response_model = SavedCardTileResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params: dict[str, QueryParamValue] = {
            "latField": self.lat_field,
            "lonField": self.lon_field,
        }
        if self.parameters is not None:
            params["parameters"] = self.parameters
        return params


class GetDashboardCardTileRequest(EndpointRequest[DashboardCardTileResponse]):
    dashboard_id: int | str
    dashcard_id: int | str
    card_id: int | str
    zoom: int
    x: int
    y: int
    lat_field: str
    lon_field: str
    parameters: str | None = None

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/tiles/{dashboard_id}/dashcard/{dashcard_id}/card/{card_id}/{zoom}/{x}/{y}"
    response_model = DashboardCardTileResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params: dict[str, QueryParamValue] = {
            "latField": self.lat_field,
            "lonField": self.lon_field,
        }
        if self.parameters is not None:
            params["parameters"] = self.parameters
        return params


class GetAdHocQueryTileRequest(EndpointRequest[AdHocQueryTileResponse]):
    zoom: int
    x: int
    y: int
    query: str
    lat_field: str
    lon_field: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/tiles/{zoom}/{x}/{y}"
    response_model = AdHocQueryTileResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return {
            "query": self.query,
            "latField": self.lat_field,
            "lonField": self.lon_field,
        }
