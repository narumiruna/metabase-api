from __future__ import annotations

from typing import Any
from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.agent import AgentResponse


class AgentExecuteRequest(EndpointRequest[AgentResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/agent/v1/execute"
    response_model = AgentResponse


class CreateAgentDashboardRequest(EndpointRequest[AgentResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/agent/v1/dashboard"
    response_model = AgentResponse


class CreateAgentQuestionRequest(EndpointRequest[AgentResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/agent/v1/question"
    response_model = AgentResponse


class GetAgentMetricRequest(EndpointRequest[AgentResponse]):
    metric_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/agent/v1/metric/{metric_id}"
    response_model = AgentResponse


class GetAgentMetricFieldValuesRequest(EndpointRequest[AgentResponse]):
    metric_id: int | str
    field_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/agent/v1/metric/{metric_id}/field/{field_id}/values"
    response_model = AgentResponse


class AgentPingRequest(EndpointRequest[AgentResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/agent/v1/ping"
    response_model = AgentResponse


class AgentSearchRequest(EndpointRequest[AgentResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/agent/v1/search"
    response_model = AgentResponse


class GetAgentTableRequest(EndpointRequest[AgentResponse]):
    table_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/agent/v1/table/{table_id}"
    response_model = AgentResponse


class GetAgentTableFieldValuesRequest(EndpointRequest[AgentResponse]):
    table_id: int | str
    field_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/agent/v1/table/{table_id}/field/{field_id}/values"
    response_model = AgentResponse


class AgentConstructQueryRequest(EndpointRequest[AgentResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/agent/v2/construct-query"
    response_model = AgentResponse


class AgentQueryRequest(EndpointRequest[AgentResponse]):
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/agent/v2/query"
    response_model = AgentResponse
