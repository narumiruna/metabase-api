# Repository Guidelines

## Project Structure & Module Organization

This is a Python 3.14 package using a `src/` layout. Runtime code lives in `src/metabaseapi/`: `client/` contains the async HTTP client, `endpoints/requests/` contains typed endpoint request models, `endpoints/execution.py` defines request execution contracts, `cli/` contains the Typer command surface, and `settings.py` owns environment-backed configuration. Tests live in `tests/`, with short locality notes in `tests/cli/`, `tests/client/`, and `tests/endpoints/`.

## Build, Test, and Development Commands

Run commands from the repository root.

- `uv sync`: install locked runtime and development dependencies.
- `just format`: format Python code with Ruff.
- `just lint`: run Ruff lint fixes.
- `just type`: run `ty check`.
- `just test`: run pytest with verbose output and coverage over `src`.
- `just all`: run format, lint, type check, and tests.
- `just live-test`: run read-only live Metabase API checks; requires `.env` or environment variables.
- `uv build`: build package artifacts locally.

## Coding Style & Naming Conventions

Use Ruff formatting with a 120-character line length. Imports are managed by Ruff/isort with single-line imports and no relative imports. Keep annotations on production code; tests intentionally relax annotation and some exception/performance rules. Preserve small public facades: `metabaseapi.endpoints` should expose submodules, while request classes belong under `metabaseapi.endpoints.requests.<domain>`. CLI command modules should stay domain-local under `metabaseapi.cli.commands`.

## Testing Guidelines

Use pytest. Name test files `tests/test_*.py` and keep tests focused on observable contracts: CLI JSON/error behavior, settings loading, public imports, endpoint models, and async client execution. Add or update tests when changing endpoint request models, CLI output, error handling, or settings behavior. Live checks are skipped unless `METABASE_LIVE_TEST=1`; configure `METABASE_URL` and `METABASE_API_KEY` via `.env` or the environment.

## Commit & Pull Request Guidelines

Recent history uses concise Conventional Commit-style subjects such as `feat(endpoints): ...`, `feat(utils): ...`, and `test: ...`. Keep commits focused and stage only intended paths. PRs should summarize behavior changes, list verification commands run, mention live-test coverage when relevant, and note any new environment variables, Docker behavior, or release-impacting changes.

## Security & Configuration Tips

Do not commit real Metabase credentials. Use `.env.sample` as the template and keep `.env` local. Treat `METABASE_API_KEY` as required for real API calls; avoid adding live tests that mutate server state unless explicitly scoped and documented.

## MEMORY.md

- `MEMORY.md` is not auto-loaded. Check it before non-trivial debugging or design work when prior project context may matter.
- Keep entries short and reusable.
- `MEMORY.md` must use `## GOTCHA` and `## TASTE` sections.
- After a non-trivial error or discovery, add one concise entry if it will help future work.
