from __future__ import annotations

from pathlib import Path

from metabaseapi import openapi_coverage


def test_generate_report_collects_endpoints() -> None:
    summary, endpoints = openapi_coverage.generate_report(Path("tests/fixtures/api.json"))

    assert summary["total"] == 600
    assert summary["missing"] > 0
    assert len(summary["method_counts"]) >= 4
    assert any(item.path == "/api/user/current" and item.method == "GET" for item in endpoints)
    assert any(
        not item.is_convenience_covered and item.expected_convenience and item.expected_convenience.startswith("list_")
        for item in endpoints
    )


def test_markdown_report_renders() -> None:
    _, endpoints = openapi_coverage.generate_report(Path("tests/fixtures/api.json"))
    content = openapi_coverage.to_markdown(endpoints)

    assert "# OpenAPI Coverage Snapshot" in content
    assert "| method | count |" in content
    assert "| method | path | operationId | hasBody | hasParams | expectedConvenience |" in content
    assert "Missing Convenience Candidates" in content


def test_discover_cli_and_client_methods() -> None:
    client_methods = openapi_coverage.discover_convenience_methods(Path("src/metabaseapi/client.py"))
    cli_commands = openapi_coverage.discover_cli_commands(Path("src/metabaseapi/cli.py"))

    assert "get_card_typed" in client_methods
    assert "list-cards" in cli_commands
    assert "request" in cli_commands
