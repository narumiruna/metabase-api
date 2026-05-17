# Repository Guidelines

## Project scope

- `src/metabaseapi/cli/__init__.py` is the Typer CLI entry point; every CLI command should map to an explicit function.
- `src/metabaseapi/cli/runtime.py` owns the Typer app object, shared CLI parsing helpers, client execution helper, and callback configuration.
- `src/metabaseapi/client/http.py` owns async Metabase HTTP calls and exports only the canonical concrete `MetabaseClient`.
- `src/metabaseapi/client` exposes exactly one public client interface: `MetabaseClient`.
- CLI commands execute hand-written endpoint request models through `MetabaseClient.run(...)`; do not reintroduce `src/metabaseapi/client/raw` or client mixins.
- `src/metabaseapi/cli/commands` owns command implementations; command module filenames use domain/action stems such as `card.py`, `card_query.py`, and `cloud_migration.py`, without a redundant `_commands.py` suffix.
- `src/metabaseapi/wire.py` contains HTTP wire types and generic HTTP request/response models; `src/metabaseapi/endpoints/` contains hand-written typed endpoint models and request helpers split by concern.
- `src/metabaseapi/endpoints/__init__.py` exposes only endpoint submodules (`entities`, `execution`, `requests`, `responses`); do not re-export every endpoint symbol at the package top level.
- `src/metabaseapi/endpoints/requests/__init__.py` owns only the request module registry; request classes must live in domain modules such as `endpoints/requests/card.py`.
- Do not reintroduce `api.json`, OpenAPI snapshot fixtures, runtime endpoint registries, or file-scanning behavior to decide API capabilities.
- This is a new project with no compatibility users; prefer breaking refactors that produce a cleaner interface over preserving shims or transitional APIs.
- 命名規範：對外公開進入點只使用 `metabaseapi.cli`（package）、`metabaseapi.client` 與 `metabaseapi.endpoints`；`metabaseapi.client.http` 為唯一 concrete client 實作入口；endpoint 呼叫直接使用 `metabaseapi.endpoints.requests` 搭配 `MetabaseClient.run(...)`。

## Commands

- Run commands from the repository root. Use `uv sync` to install dependencies.
- Keep `uv run metabaseapi --help` working so users can discover every command and option.
- Current local required gate is Ruff plus ty only: run `uv run ruff check .` and `uv run ty check .` before finishing code changes.
- Do not run pytest unless the user explicitly asks for tests or the change specifically needs test evidence.
- `just all` remains the full aggregate gate; it also runs pytest with coverage, so do not use it for routine verification under the current workflow.
- CI also runs `uv run ruff check .`, `uv run ty check .`, and `uv run pytest -v -s --cov=src --cov-report=xml tests`.
- All Python execution and script entrypoints in this repo must use `uv run python` (or `UV_CACHE_DIR=/tmp/uv-cache uv run python`); never use bare `python` or `python3` directly for project code paths.
- 確認：專案中的 Python 路徑、腳本、臨時執行都**一定要**用 `uv run python`（可配 `UV_CACHE_DIR=/tmp/uv-cache`）執行。

## Coding rules

- Keep endpoint, client, and CLI behavior hand-written and explicit.
- When adding API capability, add focused `pydantic.BaseModel` request/response models by hand, then wire them through an explicit endpoint request flow.
- Do not hard-code secrets, API keys, or deployment URLs; use `src/metabaseapi/settings.py` and documented environment variables.

## Testing

- Tests live in `tests/test_*.py`; add or update focused tests for model validation, client dispatch, CLI behavior, and settings changes.
- Prefer `httpx.MockTransport` and Typer CLI tests over live Metabase API calls in unit tests.
- Current refactor work may finish without pytest as long as `uv run ruff check .` and `uv run ty check .` pass.

## MEMORY.md

- `MEMORY.md` is not auto-loaded. Check it before non-trivial debugging or design work when prior project context may matter.
- Keep entries short and reusable.
- `MEMORY.md` must use `## GOTCHA` and `## TASTE` sections.
- After a non-trivial error or discovery, add one concise entry if it will help future work.

## Agent skills

### Issue tracker

Issues and PRDs are tracked in GitHub Issues for `narumiruna/metabase-api`. See `docs/agents/issue-tracker.md`.

### Triage labels

Use the default five-label triage vocabulary: `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.

### Domain docs

Single-context layout: root `CONTEXT.md` plus `docs/adr/`. See `docs/agents/domain.md`.
