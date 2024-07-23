from pydantic_settings import BaseSettings, SettingsConfigDict


class NemliSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", env_prefix="NEMLI_")

    discord_token: str
    openai_api_key: str


settings = NemliSettings()  # type: ignore
