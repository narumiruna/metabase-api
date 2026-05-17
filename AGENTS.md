# Repository Guidelines

## Project Scope

This is a Python 3.14 `src/` layout package for a typed async Metabase API client and JSON-first Typer CLI. Keep README user-facing; keep this file focused on agent workflow, verification, and project boundaries.

Runtime code lives in `src/metabaseapi/`: `client/` owns the async HTTP client, `cli/` owns command registration/runtime, `endpoints/requests/` and `endpoints/responses/` own endpoint models, `endpoints/execution.py` owns the request execution contract, and `settings.py` owns environment-backed configuration. Tests live in `tests/`; use the locality notes in `tests/cli/`, `tests/client/`, and `tests/endpoints/` when moving coverage.

Do not hand-edit generated or local artifacts: `.venv/`, `.ruff_cache/`, `.pytest_cache/`, `__pycache__/`, `.coverage`, `coverage.xml`, `dist/`, or build outputs under `/tmp`.

## Commands

Run commands from the repository root.

- `uv sync`: install locked runtime and development dependencies.
- `just format`: format Python code with Ruff.
- `just lint`: run Ruff lint with fixes.
- `just type`: run `ty check`.
- `just test`: run pytest with verbose output and coverage over `src`.
- `just all`: run format, lint, type check, and tests.
- `just live-test`: run read-only live Metabase API checks; requires `.env` or environment variables.
- `uv build`: build package artifacts locally.

For CI-equivalent non-mutating checks, prefer `uv run ruff check .`, `uv run ty check .`, and `uv run pytest -v -s --cov=src --cov-report=xml tests`.

## Coding Style & Naming Conventions

Use Ruff formatting with a 120-character line length. Imports are managed by Ruff/isort with single-line imports and no relative imports. Keep annotations on production code; tests intentionally relax annotation and some exception/performance rules. Preserve small public facades: `metabaseapi.endpoints` should expose submodules, while request classes belong under `metabaseapi.endpoints.requests.<domain>`. CLI command modules should stay domain-local under `metabaseapi.cli.commands`.

## Testing Guidelines

Use pytest. Name test files `tests/test_*.py` and keep tests focused on observable contracts: CLI JSON/error behavior, settings loading, public imports, endpoint models, and async client execution. Add or update tests when changing endpoint request models, CLI output, error handling, or settings behavior. Live checks are skipped unless `METABASE_LIVE_TEST=1`; configure `METABASE_URL` and `METABASE_API_KEY` via `.env` or the environment.

Do not add live tests that mutate a Metabase instance unless the request explicitly calls for that scope and the test is clearly isolated.

## Commit & Pull Request Guidelines

Recent history uses concise Conventional Commit-style subjects such as `feat(endpoints): ...`, `feat(utils): ...`, and `test: ...`. Keep commits focused and stage only intended paths. PRs should summarize behavior changes, list verification commands run, mention live-test coverage when relevant, and note any new environment variables, Docker behavior, or release-impacting changes.

## Security & Configuration Tips

Do not commit real Metabase credentials. Use `.env.sample` as the template and keep `.env` local. Treat `METABASE_API_KEY` as required for real API calls.

## MEMORY.md

- `MEMORY.md` is not auto-loaded. Check it before non-trivial debugging, design, or docs work when prior project context may matter.
- Keep entries short and reusable.
- `MEMORY.md` must use `## GOTCHA` and `## TASTE` sections.
- After a non-trivial error or discovery, add one concise entry if it will help future work.
