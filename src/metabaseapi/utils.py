import json
import logging
import os
from pathlib import Path
from typing import Final

import httpx

LATEST_OPENAPI_DOCUMENT_URL: Final[str] = "https://www.metabase.com/docs/latest/api.json"


logger = logging.getLogger(__name__)


def save_json(data: dict, path: Path) -> None:
    with path.open("w") as fp:
        json.dump(data, fp, indent=2)


def download_json(url: str, f: Path) -> None:
    with httpx.Client() as client:
        resp = client.get(url)
        resp.raise_for_status()
        save_json(resp.json(), f)


def download_openapi_document(base_url: str, f: Path) -> None:
    url = f"{base_url}/api/docs/openapi.json"
    download_json(url, f)


def download_openapi_document_from_env(f: Path) -> None:
    metabase_url = os.getenv("METABASE_URL")
    if metabase_url is None:
        logger.info(
            "METABASE_URL is not set. Downloading the latest OpenAPI document from the official Metabase website."
        )
        metabase_url = LATEST_OPENAPI_DOCUMENT_URL

    download_openapi_document(metabase_url, f)
