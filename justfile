[default]
all: format lint type test

# Format code using ruff
format:
    uv run ruff format

# Lint code using ruff
lint:
    uv run ruff check --fix

# Type checking using ty
type:
    uv run ty check

# Run tests using pytest with coverage
test:
    uv run pytest -v -s --cov=src tests

# Run live endpoint smoke tests (requires METABASE_URL + METABASE_API_KEY in environment/.env)
live-test METHODS='GET' LIMIT='':
    [ -n "{{LIMIT}}" ] && \
      uv run python scripts/live_endpoint_smoke_test.py --methods "{{METHODS}}" --limit "{{LIMIT}}" || \
      uv run python scripts/live_endpoint_smoke_test.py --methods "{{METHODS}}"

# Build and publish the package to PyPI
publish:
    uv build
    uv publish
