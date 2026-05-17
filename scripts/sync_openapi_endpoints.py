#!/usr/bin/env python3
from __future__ import annotations

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC_PATH = ROOT / "src"


def _ensure_sys_path() -> None:
    if str(SRC_PATH) not in sys.path:
        sys.path.insert(0, str(SRC_PATH))


def write_coverage_report(output_path: Path, spec_path: Path | None = None) -> None:
    _ensure_sys_path()
    from metabaseapi.openapi_coverage import generate_report
    from metabaseapi.openapi_coverage import to_markdown

    _summary, endpoints = generate_report(spec_path=spec_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(to_markdown(endpoints), encoding="utf-8")


def main() -> None:
    spec_path = ROOT / "tests" / "fixtures" / "api.json"
    output = ROOT / "docs" / "endpoint-coverage.md"
    write_coverage_report(output, spec_path=spec_path)


if __name__ == "__main__":
    main()
