from __future__ import annotations

from typing import Any
from typing import ClassVar
from typing import cast

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_dependencies import EeDependencyBackfillStatusResponse
from metabaseapi.endpoints.responses.ee_dependencies import EeDependencyCheckResponse
from metabaseapi.endpoints.responses.ee_dependencies import EeDependencyEntitiesResponse
from metabaseapi.endpoints.responses.ee_dependencies import EeDependencyGraphResponse
from metabaseapi.wire import QueryParamValue


class GetEeDependenciesBackfillStatusRequest(EndpointRequest[EeDependencyBackfillStatusResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/dependencies/backfill-status"
    response_model = EeDependencyBackfillStatusResponse


class CheckEeDependenciesCardRequest(EndpointRequest[EeDependencyCheckResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/dependencies/check-card"
    response_model = EeDependencyCheckResponse


class CheckEeDependenciesSnippetRequest(EndpointRequest[EeDependencyCheckResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/dependencies/check-snippet"
    response_model = EeDependencyCheckResponse


class CheckEeDependenciesTransformRequest(EndpointRequest[EeDependencyCheckResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/dependencies/check-transform"
    response_model = EeDependencyCheckResponse


class GetEeDependenciesGraphRequest(EndpointRequest[EeDependencyGraphResponse]):
    entity_id: int | str
    entity_type: str
    extra_params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/dependencies/graph"
    response_model = EeDependencyGraphResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params = dict(self.extra_params)
        params.update({"id": self.entity_id, "type": self.entity_type})
        return params


class GetEeDependenciesGraphBreakingRequest(EndpointRequest[EeDependencyEntitiesResponse]):
    extra_params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/dependencies/graph/breaking"
    response_model = EeDependencyEntitiesResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        return self.extra_params


class GetEeDependenciesGraphBrokenRequest(EndpointRequest[EeDependencyEntitiesResponse]):
    entity_id: int | str
    entity_type: str
    extra_params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/dependencies/graph/broken"
    response_model = EeDependencyEntitiesResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params = dict(self.extra_params)
        params.update({"id": self.entity_id, "type": self.entity_type})
        return params


class GetEeDependenciesGraphDependentsRequest(EndpointRequest[EeDependencyEntitiesResponse]):
    entity_id: int | str
    entity_type: str
    extra_params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/dependencies/graph/dependents"
    response_model = EeDependencyEntitiesResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params = dict(self.extra_params)
        params.update({"id": self.entity_id, "type": self.entity_type})
        return params


class GetEeDependenciesGraphUnreferencedRequest(EndpointRequest[EeDependencyEntitiesResponse]):
    entity_type: str | None = None
    extra_params: dict[str, QueryParamValue] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/dependencies/graph/unreferenced"
    response_model = EeDependencyEntitiesResponse

    def request_params(self) -> dict[str, QueryParamValue]:
        params = dict(self.extra_params)
        if self.entity_type is not None:
            params["type"] = cast("QueryParamValue", self.entity_type)
        return params
