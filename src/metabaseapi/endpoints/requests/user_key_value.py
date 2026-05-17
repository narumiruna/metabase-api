from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.execution import _ResponseModel
from metabaseapi.endpoints.responses.common import GenericOperationResponse
from metabaseapi.wire import JSONValue


class GetUserKeyValueNamespaceRequest(EndpointRequest[GenericOperationResponse]):
    namespace: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/user-key-value/namespace/{namespace}"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse


class PutUserKeyValueNamespaceKeyRequest(EndpointRequest[GenericOperationResponse]):
    namespace: str
    key: str
    body: JSONValue | None = None

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/user-key-value/namespace/{namespace}/key/{key}"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse


class GetUserKeyValueNamespaceKeyRequest(EndpointRequest[GenericOperationResponse]):
    namespace: str
    key: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/user-key-value/namespace/{namespace}/key/{key}"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse


class DeleteUserKeyValueNamespaceKeyRequest(EndpointRequest[GenericOperationResponse]):
    namespace: str
    key: str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/user-key-value/namespace/{namespace}/key/{key}"
    response_model: ClassVar[_ResponseModel] = GenericOperationResponse
