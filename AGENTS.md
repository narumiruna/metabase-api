# Repository Guidelines

## Project scope

- `src/metabaseapi/cli/__init__.py` is the Typer CLI entry point; every CLI command should map to an explicit function.
- `src/metabaseapi/client/http.py` owns async Metabase HTTP calls and is the canonical implementation module.
- `src/metabaseapi/client` exposes the public client exports by re-exporting the canonical implementation.
- `src/metabaseapi/cli_commands` owns command implementations; command modules are discoverable through `src/metabaseapi/cli_commands/__init__.py`.
- `src/metabaseapi/models.py` contains generic raw request/response wrappers; `src/metabaseapi/metabase/` contains hand-written typed endpoint models and request helpers split by concern.
- Do not reintroduce `api.json`, OpenAPI snapshot fixtures, runtime endpoint registries, or file-scanning behavior to decide API capabilities.
- 命名規範：對外公開進入點只使用 `metabaseapi.cli`（package）與 `metabaseapi.client`；`metabaseapi.client.http` 為唯一實作入口；`metabaseapi.client.raw`、`metabaseapi.client.typed` 僅作模組化拆分，並不作向下相容入口。

## Commands

- Run commands from the repository root. Use `uv sync` to install dependencies.
- Keep `uv run metabaseapi --help` working so users can discover every command and option.
- Use `just all` as the local aggregate gate; it runs Ruff format, Ruff lint with fixes, ty type checking, and pytest with coverage.
- CI also runs `uv run ruff check .`, `uv run ty check .`, and `uv run pytest -v -s --cov=src --cov-report=xml tests`.
- Always run Python code paths through `uv run python` (or `UV_CACHE_DIR=/tmp/uv-cache uv run python`) so dependency environment is consistent with the project.
- 確認：專案中的 Python 路徑、腳本、臨時執行都**一定要**用 `uv run python`（可配 `UV_CACHE_DIR=/tmp/uv-cache`）執行。

## Coding rules

- Keep endpoint, client, and CLI behavior hand-written and explicit.
- When adding API capability, add focused `pydantic.BaseModel` request/response models by hand, then wire them through a clear client method or raw HTTP flow.
- Do not hard-code secrets, API keys, or deployment URLs; use `src/metabaseapi/settings.py` and documented environment variables.

## Testing

- Tests live in `tests/test_*.py`; add or update focused tests for model validation, client dispatch, CLI behavior, and settings changes.
- Prefer `httpx.MockTransport` and Typer CLI tests over live Metabase API calls in unit tests.

## MEMORY.md

- `MEMORY.md` is not auto-loaded. Check it before non-trivial debugging or design work when prior project context may matter.
- Keep entries short and reusable.
- `MEMORY.md` must use `## GOTCHA` and `## TASTE` sections.
- After a non-trivial error or discovery, add one concise entry if it will help future work.
