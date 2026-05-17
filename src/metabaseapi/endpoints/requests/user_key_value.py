from __future__ import annotations

from typing import ClassVar

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.user_key_value import DeleteUserKeyValueResponse
from metabaseapi.endpoints.responses.user_key_value import UserKeyValueNamespaceResponse
from metabaseapi.endpoints.responses.user_key_value import UserKeyValueResponse
from metabaseapi.endpoints.responses.user_key_value import UserKeyValueStoreResponse
from metabaseapi.wire import JSONValue


class GetUserKeyValueNamespaceRequest(EndpointRequest[UserKeyValueNamespaceResponse]):
    namespace: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/user-key-value/namespace/{namespace}"
    response_model = UserKeyValueNamespaceResponse


class PutUserKeyValueNamespaceKeyRequest(EndpointRequest[UserKeyValueStoreResponse]):
    namespace: str
    key: str
    body: JSONValue | None = None

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/user-key-value/namespace/{namespace}/key/{key}"
    response_model = UserKeyValueStoreResponse


class GetUserKeyValueNamespaceKeyRequest(EndpointRequest[UserKeyValueResponse]):
    namespace: str
    key: str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/user-key-value/namespace/{namespace}/key/{key}"
    response_model = UserKeyValueResponse


class DeleteUserKeyValueNamespaceKeyRequest(EndpointRequest[DeleteUserKeyValueResponse]):
    namespace: str
    key: str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/user-key-value/namespace/{namespace}/key/{key}"
    response_model = DeleteUserKeyValueResponse
