from __future__ import annotations

import asyncio
from typing import Any
from typing import ClassVar

from pydantic import BaseModel

from metabaseapi.endpoints.execution import EndpointRequest
from scripts.audit_openapi_endpoints import ImplementedOperations
from scripts.audit_openapi_endpoints import OpenAPIOperations
from scripts.audit_openapi_endpoints import query_param_gaps


class _AuditResponse(BaseModel):
    pass


class _GenericTransportRequest(EndpointRequest[_AuditResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/example"
    response_model = _AuditResponse


class _NoGenericTransportRequest(EndpointRequest[_AuditResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/example"
    response_model = _AuditResponse

    async def do(self, client: Any) -> _AuditResponse:
        _ = client
        await asyncio.sleep(0)
        return _AuditResponse()


def test_query_param_audit_accepts_inherited_params_with_base_transport() -> None:
    openapi_operations: OpenAPIOperations = {
        ("GET", "/api/example"): [("/api/example", {}, [{"in": "query", "name": "status"}])],
    }
    implemented_operations: ImplementedOperations = {
        ("GET", "/api/example"): [
            ("tests.test_openapi_audit", "_GenericTransportRequest", _GenericTransportRequest, "/api/example"),
        ],
    }

    assert query_param_gaps(openapi_operations, implemented_operations) == []


def test_query_param_audit_flags_inherited_params_without_base_transport() -> None:
    openapi_operations: OpenAPIOperations = {
        ("GET", "/api/example"): [("/api/example", {}, [{"in": "query", "name": "status"}])],
    }
    implemented_operations: ImplementedOperations = {
        ("GET", "/api/example"): [
            ("tests.test_openapi_audit", "_NoGenericTransportRequest", _NoGenericTransportRequest, "/api/example"),
        ],
    }

    assert query_param_gaps(openapi_operations, implemented_operations) == [
        ("tests.test_openapi_audit", "_NoGenericTransportRequest", "/api/example", "/api/example", ["status"]),
    ]
