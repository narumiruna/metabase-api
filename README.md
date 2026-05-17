# metabase-api

> Async-first Python client and CLI for the [Metabase](https://www.metabase.com/) REST API.

[![Python 3.14+](https://img.shields.io/badge/python-3.14%2B-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

**metabase-api** is a lightweight Python library and CLI for the Metabase REST API. Built on [httpx](https://www.python-httpx.org/) and [Typer](https://typer.tiangolo.com/), it gives you typed request/response models and a clean terminal interface — perfect for automation, scripting, and AI-driven data workflows.

---

## 📚 Table of contents

- [✨ Features](#-features)
- [📋 Requirements](#-requirements)
- [📦 Installation](#-installation)
- [⚙️ Configuration](#%EF%B8%8F-configuration)
- [🚀 Quick start](#-quick-start)
- [🖥️ CLI reference](#%EF%B8%8F-cli-reference)
- [📊 API coverage](#-api-coverage)
- [🛠️ Development](#%EF%B8%8F-development)
- [📄 License](#-license)

---

## ✨ Features

- ⚡ **Async-first HTTP client** — powered by `httpx`, suitable for high-concurrency automation scripts.
- 🔷 **Typed models** — every request and response is a `pydantic.BaseModel`; no code generation.
- 🖥️ **Ergonomic CLI** — discover and run Metabase operations directly from the terminal with `metabaseapi <command>`.
- 📄 **Pretty JSON output** — all CLI commands emit indented, sorted JSON, ready for use with `jq` or AI pipelines.
- 🔑 **API key authentication** — uses Metabase's native API key header; no session tokens to manage.
- 🔒 **TLS-aware** — configurable SSL verification for self-hosted deployments.

---

## 📋 Requirements

- 🐍 Python ≥ 3.14
- 🗄️ A running Metabase instance (self-hosted or Metabase Cloud)
- 🔑 A Metabase API key (Settings → Admin → API Keys)

---

## 📦 Installation

Install with [uv](https://docs.astral.sh/uv/) (recommended):

```bash
uv sync
```

Or install from source with pip:

```bash
pip install .
```

---

## ⚙️ Configuration

Set the following environment variables before running any command or using the client:

| Variable | Description | Default |
|---|---|---|
| `METABASE_URL` | Base URL of your Metabase instance | `http://localhost:3000` |
| `METABASE_API_KEY` | Metabase API key for authentication | *(required)* |
| `METABASE_TIMEOUT_SECONDS` | HTTP request timeout in seconds | `30.0` |
| `METABASE_VERIFY_SSL` | Verify TLS certificates (`true`/`false`) | `true` |

Export them in your shell or add them to a `.env` file (see `.env.sample`):

```bash
export METABASE_URL=https://your-metabase.example.com
export METABASE_API_KEY=your-api-key
```

---

## 🚀 Quick start

```bash
# Who am I?
metabaseapi current-user

# List all databases
metabaseapi list-databases

# Get a specific card (question)
metabaseapi get-card 2

# List dashboards
metabaseapi list-dashboards
```

All output is valid JSON, so you can pipe it directly to `jq`:

```bash
metabaseapi list-databases | jq '.[].name'
```

---

## 🖥️ CLI reference

Run `metabaseapi --help` to see all available commands. Common examples:

```bash
# Users & auth
metabaseapi current-user
metabaseapi list-users
metabaseapi get-user 4

# Databases
metabaseapi list-databases
metabaseapi get-database 1
metabaseapi create-database my_db postgres --details '{"host":"localhost","port":5432}'

# Cards (questions / models)
metabaseapi list-cards
metabaseapi get-card 2
metabaseapi create-card Orders '{"database":1,"type":"query","query":{"source-table":2}}' --type question
metabaseapi create-question Orders '{"database":1,"type":"query","query":{"source-table":2}}'

# Dashboards
metabaseapi list-dashboards
metabaseapi get-dashboard 1

# Collections
metabaseapi list-collections
metabaseapi get-collection root

# Tables & fields
metabaseapi list-tables
metabaseapi get-table 8
metabaseapi get-field 9
```

Every command outputs pretty-printed, sorted JSON — suitable for AI agents, shell scripts, and CI pipelines.

---

## 📊 API coverage

`docs/TODO.md` tracks implementation status against the official Metabase API documentation (600 documented operations).

**Current status: 152 / 600 endpoints fully implemented.**

An endpoint counts as complete when it has:
1. A hand-written endpoint request model runnable with `MetabaseClient.run(...)`
2. A typed `pydantic.BaseModel` for both request and response
3. A corresponding CLI command

Raw `request` / `invoke` passthroughs are intentionally excluded — every operation must be explicitly modelled.

---

## 🛠️ Development

```bash
# Install all dependencies (including dev)
uv sync

# Lint
uv run ruff check .

# Type-check
uv run ty check .

# Run tests
uv run pytest -v -s --cov=src --cov-report=xml tests

# Full gate (lint + type-check + tests + coverage)
just all

# Low-risk read-only live smoke test (requires .env)
just live-test
```

---

## 📄 License

[MIT](LICENSE) © narumi
