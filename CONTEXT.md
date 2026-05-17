# Metabase API Client Context

This repository builds an async Python client and CLI for the Metabase HTTP API. Runtime behavior is intentionally explicit and hand-written.

## Language

**Hand-written endpoint model**:
A `pydantic.BaseModel` request or response class checked into source and maintained by humans.

**Raw HTTP request**:
The generic CLI/client path that accepts a method and path, validates the method, and executes it with `httpx.AsyncClient`.

**Convenience command**:
A CLI command or client method that gives a named shortcut for one Metabase API path instead of requiring a raw method/path input.

## Relationships

- A **Convenience command** maps to explicit hand-written client code.
- A **Hand-written endpoint model** can provide typed request/response parsing for high-value endpoints.
- The **Raw HTTP request** path keeps the CLI useful while new convenience commands are added deliberately.

## Example dialogue

> **Dev:** "Should `metabaseapi.cli` create commands implicitly?"
> **Domain expert:** "No — CLI behavior stays explicit. Add commands and models by hand."

## Flagged ambiguities

- API surface growth is intentionally manual. When adding a new endpoint, prefer one focused model/test pair over broad scaffolding.
