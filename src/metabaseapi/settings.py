from __future__ import annotations

from pydantic import Field
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
        populate_by_name=True,
    )

    base_url: str = Field(default="http://localhost:3000", alias="METABASE_URL")
    api_key: str | None = Field(default=None, alias="METABASE_API_KEY")
    timeout_seconds: float = Field(default=30.0, alias="METABASE_TIMEOUT_SECONDS")
    verify_ssl: bool = Field(default=True, alias="METABASE_VERIFY_SSL")

    def requires_api_key(self) -> str:
        if not self.api_key:
            raise ValueError("METABASE_API_KEY is required")
        return self.api_key


def load_runtime_settings(
    *,
    base_url: str | None = None,
    api_key: str | None = None,
    timeout_seconds: float | None = None,
    verify_ssl: bool | None = None,
) -> Settings:
    base = Settings()
    values = base.model_dump()
    if base_url is not None:
        values["base_url"] = base_url
    if api_key is not None:
        values["api_key"] = api_key
    if timeout_seconds is not None:
        values["timeout_seconds"] = timeout_seconds
    if verify_ssl is not None:
        values["verify_ssl"] = verify_ssl
    return Settings(**values)


settings = Settings()
