#!/usr/bin/env python3
from __future__ import annotations

import argparse
import asyncio
import json
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

import httpx

from metabaseapi import settings

SupportedMethod = str


@dataclass(frozen=True)
class EndpointCheck:
    method: str
    template_path: str
    concrete_path: str
    status_code: int | None
    result: str
    error: str | None = None


def parse_methods(raw: str) -> list[SupportedMethod]:
    methods: list[SupportedMethod] = []
    for item in raw.split(","):
        method = item.strip().upper()
        if not method:
            continue
        if method not in {"DELETE", "GET", "POST", "PUT", "PATCH"}:
            raise ValueError(f"Unsupported method: {method}")
        methods.append(method)

    return methods


def load_openapi_endpoints(spec_path: Path, methods: list[SupportedMethod]) -> list[tuple[str, str]]:
    raw = json.loads(spec_path.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        return []

    paths = raw.get("paths", {})
    if not isinstance(paths, dict):
        return []

    selected = set(methods)
    items: list[tuple[str, str]] = []
    for path, operations in paths.items():
        if not isinstance(operations, dict):
            continue
        for method in operations:
            method_upper = str(method).upper()
            if method_upper not in selected:
                continue
            if not isinstance(path, str):
                continue
            items.append((method_upper, path))

    # deterministic order for easier diffing
    return sorted(items, key=lambda item: (item[0], item[1]))


def fill_template_path(path: str) -> str:
    segments = [segment for segment in path.strip("/").split("/") if segment]
    if not segments:
        return "/"

    concrete_segments: list[str] = []
    for segment in segments:
        if segment.startswith("{") and segment.endswith("}"):
            key = segment[1:-1]
            value = placeholder_value(key)
            concrete_segments.append(quote(value, safe=""))
        else:
            concrete_segments.append(segment)

    return "/" + "/".join(concrete_segments)


def placeholder_value(segment: str) -> str:
    name = segment.lower()

    if name in {"yyyy-mm", "year-month"}:
        return "2026-05"
    if "uuid" in name:
        return "00000000-0000-0000-0000-000000000000"
    if "token" in name:
        return "demo-token"
    if name in {"id", "uuid", "query", "name", "key", "namespace", "slug", "path", "schema", "table", "type"}:
        return "sample"
    if "id" in name:
        return "1"

    return "sample"


def classify_status(status_code: int, *, strict: bool) -> str:
    if strict:
        return "pass" if 200 <= status_code < 300 else "fail"

    if 500 <= status_code < 600:
        return "fail"
    if 200 <= status_code < 300:
        return "pass"
    return "warn"


async def run_live_checks(
    *,
    method_filters: list[SupportedMethod],
    spec_path: Path,
    limit: int | None,
    strict: bool,
    timeout_seconds: float,
    max_failures: int | None,
    runtime: settings.Settings,
) -> int:
    api_key = runtime.requires_api_key()

    endpoints = load_openapi_endpoints(spec_path, method_filters)
    if limit is not None:
        endpoints = endpoints[:limit]

    checks: list[EndpointCheck] = []
    headers = {"X-API-Key": api_key, "Accept": "application/json"}

    async with httpx.AsyncClient(timeout=httpx.Timeout(timeout=timeout_seconds), verify=runtime.verify_ssl) as client:
        for method, template_path in endpoints:
            concrete_path = fill_template_path(template_path)
            url = runtime.base_url.rstrip("/") + concrete_path
            status_code: int | None = None
            error: str | None = None

            try:
                response = await client.request(
                    method,
                    url,
                    headers=headers,
                    json={"name": "sample"} if method in {"POST", "PUT", "PATCH"} else None,
                )
                status_code = response.status_code
                result = classify_status(status_code, strict=strict)
            except httpx.TimeoutException:
                error = "timeout"
                result = "fail"
            except httpx.NetworkError as exc:
                error = f"network: {exc!s}"
                result = "fail"

            checks.append(
                EndpointCheck(
                    method=method,
                    template_path=template_path,
                    concrete_path=concrete_path,
                    status_code=status_code,
                    result=result,
                    error=error,
                ),
            )

            status_text = "-" if status_code is None else str(status_code)
            details = f" {error}" if error else ""
            print(f"[{result:>4}] {method:>5} {status_text:>3} {concrete_path}{details}")

    passes = sum(1 for item in checks if item.result == "pass")
    warns = sum(1 for item in checks if item.result == "warn")
    fails = sum(1 for item in checks if item.result == "fail")

    print(f"\n[summary] total={len(checks)} pass={passes} warn={warns} fail={fails}")

    if max_failures is not None:
        return 1 if fails > max_failures else 0
    return 1 if fails else 0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run live smoke checks against OpenAPI endpoints.")
    parser.add_argument(
        "--spec",
        default="tests/fixtures/api.json",
        type=Path,
        help="Path to OpenAPI fixture JSON.",
    )
    parser.add_argument("--methods", default="GET", help="Comma-separated methods to test (e.g. GET,POST).")
    parser.add_argument("--limit", type=int, default=None, help="Optional maximum number of endpoints to test.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat any non-2xx response as failure.",
    )
    parser.add_argument(
        "--max-failures",
        type=int,
        default=None,
        help="Allow this many failures before returning non-zero. Default: fail on any fail.",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=None,
        help="Override request timeout seconds (fallback to METABASE_TIMEOUT_SECONDS).",
    )
    return parser.parse_args()


async def main() -> None:
    args = parse_args()
    methods = parse_methods(args.methods)

    settings_obj = settings.load_runtime_settings(timeout_seconds=args.timeout)
    timeout_seconds = settings_obj.timeout_seconds

    exit_code = await run_live_checks(
        method_filters=methods,
        spec_path=args.spec,
        limit=args.limit,
        strict=args.strict,
        timeout_seconds=timeout_seconds,
        max_failures=args.max_failures,
        runtime=settings_obj,
    )
    raise SystemExit(exit_code)


if __name__ == "__main__":
    asyncio.run(main())
