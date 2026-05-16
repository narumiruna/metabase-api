from pydantic import Field
from pydantic_settings import BaseSettings
from pydantic_settings import SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore",
    )

    METABASE_URL: str = Field(default="http://localhost:3000")
    METABASE_API_KEY: str = Field(...)


settings = Settings()
