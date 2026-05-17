from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.ee_cloud import EeCloudAddOnOperationResponse
from metabaseapi.endpoints.responses.ee_cloud import EeCloudAddOnsResponse
from metabaseapi.endpoints.responses.ee_cloud import EeCloudPlansResponse
from metabaseapi.endpoints.responses.ee_cloud import EeCloudProxyResponse


class GetEeCloudAddOnsAddonsRequest(EndpointRequest[EeCloudAddOnsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/cloud-add-ons/addons"
    response_model = EeCloudAddOnsResponse


class GetEeCloudAddOnsPlansRequest(EndpointRequest[EeCloudPlansResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/ee/cloud-add-ons/plans"
    response_model = EeCloudPlansResponse


class PostEeCloudAddOnsProductTypeRequest(EndpointRequest[EeCloudAddOnOperationResponse]):
    product_type: str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/cloud-add-ons/{product_type}"
    response_model = EeCloudAddOnOperationResponse


class DeleteEeCloudAddOnsProductTypeRequest(EndpointRequest[EeCloudAddOnOperationResponse]):
    product_type: str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/ee/cloud-add-ons/{product_type}"
    response_model = EeCloudAddOnOperationResponse


class PostEeCloudProxyOperationIdRequest(EndpointRequest[EeCloudProxyResponse]):
    operation_id: str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/ee/cloud-proxy/{operation_id}"
    response_model = EeCloudProxyResponse
