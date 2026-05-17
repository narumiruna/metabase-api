# OpenAPI Endpoint Audit

This document records the workflow used to download the active Metabase OpenAPI document and verify that `src/metabaseapi/endpoints/requests/` endpoint request models are aligned with it.

## Purpose

- Download `/api/docs/openapi.json` from the configured `METABASE_URL` with `metabaseapi.utils.download_openapi_document_from_env`.
- Compare OpenAPI HTTP method + path pairs with all `EndpointRequest` subclasses.
- Verify that each request class can handle its OpenAPI path placeholders, request body, and query parameters.

## Prerequisites

1. Run commands from the repository root.
2. Configure `METABASE_URL` through `.env` or the shell environment, for example:

   ```bash
   export METABASE_URL="http://localhost:3000"
   ```

3. Use `uv run` for project Python commands.

> Downloading the OpenAPI document only needs `METABASE_URL`. Do not commit real API keys or local downloaded files that may contain environment-specific details.

## Audit script

The audit script lives at:

```text
scripts/audit_openapi_endpoints.py
```

Run it with:

```bash
UV_CACHE_DIR=/tmp/uv-cache uv run scripts/audit_openapi_endpoints.py
```

By default, the downloaded OpenAPI document is written to `/tmp/metabase-api-openapi.json`. Use `--output` to choose another path:

```bash
UV_CACHE_DIR=/tmp/uv-cache uv run scripts/audit_openapi_endpoints.py --output /tmp/openapi.json
```

Use `--details` when a gap counter is non-zero and you need the failing entries:

```bash
UV_CACHE_DIR=/tmp/uv-cache uv run scripts/audit_openapi_endpoints.py --details
```

## Reading the output

A successful audit requires all four gap counters to be `0`:

- `missing_openapi_operations`: an OpenAPI method + path does not have a matching request class.
- `placeholder_gaps`: an `endpoint_path` placeholder, such as `{id}`, does not have a corresponding Pydantic model field.
- `request_body_gaps`: OpenAPI declares `requestBody`, but the request class has no `body` field and does not override `request_body()`.
- `query_param_gaps`: OpenAPI declares query parameters, but the request class has no generic `params` field, no matching named fields, and no custom `request_params()` implementation.

`implemented_unique_operations` may be larger than `openapi_operations` because this package can include newer, enterprise, or otherwise environment-specific endpoints that are not present in the downloaded OpenAPI document.

## Baseline from this audit

This was the result after downloading the active document with `download_openapi_document_from_env`:

```text
downloaded_openapi_bytes 1464496
openapi_version 3.1.0 v0.61.1.4
openapi_paths 390
openapi_operations 477
implemented_unique_operations 608
missing_openapi_operations 0
placeholder_gaps 0
request_body_gaps 0
query_param_gaps 0
```

## Verification after fixes

After endpoint fixes, run at least:

```bash
UV_CACHE_DIR=/tmp/uv-cache just all
```

For a narrower rerun, first run the audit script, then run the relevant checks:

```bash
UV_CACHE_DIR=/tmp/uv-cache uv run ruff check .
UV_CACHE_DIR=/tmp/uv-cache uv run ty check .
UV_CACHE_DIR=/tmp/uv-cache uv run pytest -q tests/test_endpoints_models.py tests/test_import_contracts.py
```
