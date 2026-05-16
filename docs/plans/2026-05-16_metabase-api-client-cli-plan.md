## Goal

Implement an async-first Python Metabase API client and Typer CLI that authenticate with Metabase API keys, issue Metabase API requests, and print JSON responses in an AI-readable format. Success means the package exposes a reusable async client, the `metabaseapi` console script can call documented Metabase endpoints, and the repository quality gate passes.

## Context

- Current repository is a minimal Python package with `httpx`, `pydantic`, `pydantic-settings`, and `typer` already configured in `pyproject.toml`.
- `OBJECTIVES.md` points to `https://metabase.com/docs/latest/api` and requires an async-first client plus CLI.
- Metabase publishes `https://www.metabase.com/docs/latest/api.json`, an OpenAPI 3.1 document with hundreds of paths and API-key auth via the `X-API-Key` header.
- Metabase states its API is not versioned, so implementation should avoid assuming the latest hosted spec is permanently stable.

## Architecture

- Add a thin async HTTP client layer around `httpx.AsyncClient` for base URL normalization, authentication headers, request execution, JSON parsing, and error mapping.
- Keep the CLI as a small Typer adapter that loads settings/options, delegates requests to the async client, and prints deterministic formatted JSON.
- Use the OpenAPI `api.json` as an endpoint catalog and test reference, but keep a generic request method so unsupported or newly added Metabase endpoints remain usable before typed wrappers exist.

## Non-Goals

- Do not implement typed wrappers for every Metabase endpoint in the first pass.
- Do not implement interactive login/session-cookie authentication unless API-key auth proves insufficient for required endpoints.
- Do not require a live Metabase server for the default unit test suite.

## Unknowns

- Which endpoint groups need first-class typed convenience methods beyond generic requests; resolve by implementing a small initial set and expanding after user feedback.
- Whether a pinned copy of `api.json` should be committed or only used in tests/docs; resolve before adding generated code or endpoint validation that depends on the spec.

## Plan

- [x] Inspect `https://www.metabase.com/docs/latest/api.json` for authentication, common response shapes, and representative endpoint groups; verify with a done note in `docs/plans/2026-05-16_metabase-api-client-cli-plan.md` or a committed spec snapshot if chosen.
- [x] Update settings/configuration to support `METABASE_URL`, `METABASE_API_KEY`, timeout, and optional TLS verification without importing required secrets at module import time; verify with unit tests that instantiate settings from environment overrides.
- [x] Add `src/metabaseapi/client.py` with an async `MetabaseClient` supporting context-manager use and generic `request/get/post/put/delete` methods that attach `X-API-Key`; verify with mocked `httpx` tests that assert URL joining, headers, query params, JSON bodies, and response parsing.
- [x] Add domain-specific exceptions for HTTP status errors, network errors, and non-JSON responses to produce actionable responses; verify with tests that simulate 4xx/5xx, timeout, and invalid JSON responses.
- [x] Add `src/metabaseapi/models.py` with `pydantic.BaseModel` models for request/response structures and payload typing.
- [x] Add a small initial convenience API surface for high-value read operations such as `current_user()`, `list_databases()`, `get_dashboard(id)`, and `get_card(id)`; verify each method maps to the documented OpenAPI path using mocked requests.
- [x] Replace the placeholder Typer command in `src/metabaseapi/cli.py` with async-backed commands for raw requests plus selected convenience commands that print sorted, indented JSON; verify with `typer.testing.CliRunner` tests for exit codes, output format, env loading, and error output.
- [x] Document installation, environment variables, CLI examples, and client usage in `README.md`; verify examples are consistent with `pyproject.toml` script name and implemented commands.
- [x] Run formatting, linting, typing, and tests through the repository gate `just` or the equivalent `uv run ruff format && uv run ruff check && uv run ty check && uv run pytest -v -s --cov=src tests`; verify all commands pass.

## Risks

- The hosted Metabase OpenAPI document can change without versioning, so generated or hard-coded endpoint assumptions may drift.
- Some Metabase endpoints may return binary exports or non-JSON payloads, which conflicts with the CLI's default JSON output assumption.
- Requiring `METABASE_API_KEY` at import time can break CLI help and tests if settings are loaded too early.

## Rollback / Recovery

- Keep the initial implementation additive and generic: if a typed convenience method is wrong, remove or fix that method while preserving the generic request path.
- If the latest hosted OpenAPI spec breaks tests, pin a known-good spec snapshot under `docs/` or `tests/fixtures/` and compare updates explicitly.

## Completion Checklist

- [x] Async client authentication and request behavior are verified by mocked unit tests covering headers, URL joining, params, JSON bodies, and parsed JSON responses.
- [x] CLI JSON output and failure behavior are verified by `typer.testing.CliRunner` tests with no live Metabase dependency.
- [x] README usage instructions are verified against implemented command names and environment variables.
- [x] Repository quality gate passes with `just` or equivalent `uv run` formatting, linting, type checking, and pytest commands.
