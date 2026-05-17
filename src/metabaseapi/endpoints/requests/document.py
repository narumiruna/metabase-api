from __future__ import annotations

from typing import Any
from typing import ClassVar

from pydantic import Field as PydanticField

from metabaseapi.endpoints.execution import EndpointRequest
from metabaseapi.endpoints.responses.document import CreateDocumentPublicLinkResponse
from metabaseapi.endpoints.responses.document import DeleteDocumentPublicLinkResponse
from metabaseapi.endpoints.responses.document import DeleteDocumentResponse
from metabaseapi.endpoints.responses.document import DocumentQueryExportResponse
from metabaseapi.endpoints.responses.document import DocumentResponse
from metabaseapi.endpoints.responses.document import ListDocumentsResponse
from metabaseapi.endpoints.responses.document import ListPublicDocumentsResponse
from metabaseapi.wire import JSONValue


class ListDocumentsRequest(EndpointRequest[ListDocumentsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/document"
    response_model = ListDocumentsResponse


class CreateDocumentRequest(EndpointRequest[DocumentResponse]):
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/document"
    response_model = DocumentResponse


class ListPublicDocumentsRequest(EndpointRequest[ListPublicDocumentsResponse]):
    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/document/public"
    response_model = ListPublicDocumentsResponse


class GetDocumentRequest(EndpointRequest[DocumentResponse]):
    document_id: int | str

    endpoint_method: ClassVar[str] = "GET"
    endpoint_path: ClassVar[str] = "/api/document/{document_id}"
    response_model = DocumentResponse


class UpdateDocumentRequest(EndpointRequest[DocumentResponse]):
    document_id: int | str
    body: dict[str, Any]

    endpoint_method: ClassVar[str] = "PUT"
    endpoint_path: ClassVar[str] = "/api/document/{document_id}"
    response_model = DocumentResponse


class DeleteDocumentRequest(EndpointRequest[DeleteDocumentResponse]):
    document_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/document/{document_id}"
    response_model = DeleteDocumentResponse


class DocumentCardQueryExportRequest(EndpointRequest[DocumentQueryExportResponse]):
    document_id: int | str
    card_id: int | str
    export_format: str
    body: dict[str, Any] = PydanticField(default_factory=dict)

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/document/{document_id}/card/{card_id}/query/{export_format}"
    response_model = DocumentQueryExportResponse

    def request_body(self) -> JSONValue:
        return self.body or None


class CreateDocumentPublicLinkRequest(EndpointRequest[CreateDocumentPublicLinkResponse]):
    document_id: int | str

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/document/{document_id}/public-link"
    response_model = CreateDocumentPublicLinkResponse


class DeleteDocumentPublicLinkRequest(EndpointRequest[DeleteDocumentPublicLinkResponse]):
    document_id: int | str

    endpoint_method: ClassVar[str] = "DELETE"
    endpoint_path: ClassVar[str] = "/api/document/{document_id}/public-link"
    response_model = DeleteDocumentPublicLinkResponse


class CopyDocumentRequest(EndpointRequest[DocumentResponse]):
    from_document_id: int | str
    body: dict[str, Any] | None = None

    endpoint_method: ClassVar[str] = "POST"
    endpoint_path: ClassVar[str] = "/api/document/{from_document_id}/copy"
    response_model = DocumentResponse
