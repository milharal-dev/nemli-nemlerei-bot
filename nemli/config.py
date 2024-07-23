from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class DiscordSettings(BaseModel):
    token: str
    prefix: str


class NemliSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="NEMLI_", env_nested_delimiter='__')

    discord: DiscordSettings


settings = NemliSettings()  # type: ignore
