from __future__ import annotations

from typing import Any
from typing import ClassVar
from typing import cast

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.search import SearchReindexResponse
from metabaseapi.endpoints.responses.search import SearchResponse
from metabaseapi.endpoints.responses.search import SearchWeightsResponse
from metabaseapi.endpoints.responses.search import UpdateSearchWeightsResponse
from metabaseapi.wire import QueryParamValue


class SearchRequest(EndpointRequest[SearchResponse]):
    q: str | None = None
    archived: bool | None = None
    models: list[str] | None = None
    table_db_id: int | str | None = None
    collection_id: int | str | None = None
    creator_id: int | str | None = None
    verified: bool | None = None
    include_dashboard_questions: bool | None = None
    search_native_query: bool | None = None
    context: str | None = None
    namespace: str | None = None
    limit: int | None = None
    offset: int | None = None
    extra_params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/search"
    response_model = SearchResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params = dict(self.extra_params)
        params.update(
            {
                key: cast("QueryParamValue", value)
                for key, value in (
                    ("q", self.q),
                    ("archived", self.archived),
                    ("models", self.models),
                    ("table_db_id", self.table_db_id),
                    ("collection_id", self.collection_id),
                    ("creator_id", self.creator_id),
                    ("verified", self.verified),
                    ("include_dashboard_questions", self.include_dashboard_questions),
                    ("search_native_query", self.search_native_query),
                    ("context", self.context),
                    ("namespace", self.namespace),
                    ("limit", self.limit),
                    ("offset", self.offset),
                )
                if value is not None
            }
        )
        return params


class ForceSearchReindexRequest(EndpointRequest[SearchReindexResponse]):
    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/search/force-reindex"
    response_model = SearchReindexResponse


class ReInitSearchRequest(EndpointRequest[SearchReindexResponse]):
    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/search/re-init"
    response_model = SearchReindexResponse


class GetSearchWeightsRequest(EndpointRequest[SearchWeightsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/search/weights"
    response_model = SearchWeightsResponse


class UpdateSearchWeightsRequest(EndpointRequest[UpdateSearchWeightsResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/search/weights"
    response_model = UpdateSearchWeightsResponse
