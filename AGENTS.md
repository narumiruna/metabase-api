# Repository Guidelines

## Project scope

- `src/metabaseapi/cli.py` is the Typer CLI entry point; every CLI command should map to an explicit function.
- `src/metabaseapi/client.py` owns async Metabase HTTP calls; use `httpx.AsyncClient` `get`/`post`/`put`/`patch`/`delete` methods directly.
- `src/metabaseapi/models.py` contains generic raw request/response wrappers; `src/metabaseapi/metabase/models.py` contains hand-written typed endpoint models.
- Do not reintroduce `api.json`, OpenAPI snapshot fixtures, runtime endpoint registries, or file-scanning behavior to decide API capabilities.

## Commands

- Run commands from the repository root. Use `uv sync` to install dependencies.
- Keep `uv run metabaseapi --help` working so users can discover every command and option.
- Use `just all` as the local aggregate gate; it runs Ruff format, Ruff lint with fixes, ty type checking, and pytest with coverage.
- CI also runs `uv run ruff check .`, `uv run ty check .`, and `uv run pytest -v -s --cov=src --cov-report=xml tests`.

## Coding rules

- Keep endpoint, client, and CLI behavior hand-written and explicit.
- When adding API capability, add focused `pydantic.BaseModel` request/response models by hand, then wire them through a clear client method or raw HTTP flow.
- Do not hard-code secrets, API keys, or deployment URLs; use `src/metabaseapi/settings.py` and documented environment variables.

## Testing

- Tests live in `tests/test_*.py`; add or update focused tests for model validation, client dispatch, CLI behavior, and settings changes.
- Prefer `httpx.MockTransport` and Typer CLI tests over live Metabase API calls in unit tests.
