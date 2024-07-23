from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="NEMLI_")

    DISCORD_TOKEN: str
    DISCORD_PREFIX: str


settings = Settings()  # type: ignore
