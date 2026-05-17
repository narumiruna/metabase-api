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

# Run read-only live checks against the Metabase API configured by .env
live-test:
    uv run python scripts/live_test.py

# Build and publish the package to PyPI
publish:
    uv build
    uv publish
