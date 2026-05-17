# metabaseapi: Async Python Client and CLI for the Metabase API

`metabaseapi` is a typed, async Python client and command-line interface for the
[Metabase](https://www.metabase.com/) API. It wraps Metabase endpoints with
Pydantic request and response models, uses `httpx` for async HTTP, and exposes a
JSON-first `metabaseapi` CLI for automation, inspection, and scripting.

Use this project when you need a Python Metabase API client for dashboards,
cards, databases, collections, users, settings, permissions, embedding, search,
and other Metabase administration workflows.

⚠️ This package is currently early-stage and versioned as `0.0.0`. Pin commits
or tags when using it outside local development.

## Features

- Async Metabase API client built on `httpx.AsyncClient`.
- Typed endpoint request models with Pydantic validation.
- JSON CLI output designed for scripts and agent workflows.
- Environment-based configuration via `METABASE_URL` and `METABASE_API_KEY`.
- Coverage for many core, admin, and enterprise Metabase endpoint families.
- Local tests for CLI behavior, settings, client transport, endpoint models, and
  optional live Metabase smoke checks.

## Requirements

- Python 3.14 or newer.
- `uv` for local development and dependency management.
- A Metabase instance plus an API key for real API calls.

## Installation

Install directly from GitHub when consuming the project before a packaged
release:

```bash
uv tool install git+https://github.com/narumiruna/metabase-api.git
```

For development, clone the repository and sync dependencies:

```bash
git clone https://github.com/narumiruna/metabase-api.git
cd metabase-api
uv sync
```

## Quick Start

Configure the Metabase connection with environment variables:

```bash
export METABASE_URL="http://localhost:3000"
export METABASE_API_KEY="mb_xxxxxxxxxxxxxxxxxxxx"
```

Inspect the CLI and run read-only API commands:

```bash
metabaseapi --help
metabaseapi current-user
metabaseapi list-databases
metabaseapi list-cards
metabaseapi list-dashboards
```

All successful CLI responses are rendered as formatted JSON. API and validation
errors are printed to stderr as JSON error payloads and return exit code `1`.

## Python API Example

```python
import asyncio

from metabaseapi.client import MetabaseClient
from metabaseapi.endpoints.requests.user import CurrentUserRequest
from metabaseapi.settings import Settings


async def main() -> None:
    settings = Settings()
    async with MetabaseClient.from_settings(settings) as client:
        current_user = await client.run(CurrentUserRequest())
        print(current_user.model_dump(mode="json", exclude_none=True))


asyncio.run(main())
```

Endpoint requests live under `metabaseapi.endpoints.requests.<domain>`, for
example `user`, `database`, `card`, `dashboard`, `collection`, `table`, and
`search`.

## Configuration

`metabaseapi` reads `.env` and process environment values through Pydantic
settings:

| Variable | Default | Purpose |
| --- | --- | --- |
| `METABASE_URL` | `http://localhost:3000` | Base URL for the Metabase instance. |
| `METABASE_API_KEY` | none | Required API key for real requests. |
| `METABASE_TIMEOUT_SECONDS` | `30.0` | HTTP timeout in seconds. |
| `METABASE_VERIFY_SSL` | `true` | Enable or disable TLS verification. |

Use `.env.sample` as the local template. Do not commit real API keys.

## Development

Common repository commands:

```bash
just format      # format Python code with Ruff
just lint        # run Ruff lint fixes
just type        # run `ty` type checking
just test        # run pytest with coverage
just all         # run format, lint, type, and tests
```

🧪 Optional live checks are read-only and require a configured Metabase instance:

```bash
just live-test
```

## Project Layout

```text
src/metabaseapi/
  client/                 async HTTP client
  cli/                    Typer CLI runtime and commands
  endpoints/              request models, response models, and execution contract
  settings.py             environment-backed configuration
tests/                    unit, CLI, endpoint, and optional live tests
```

## License

This project is licensed under the terms in [LICENSE](LICENSE).
