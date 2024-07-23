from pydantic_settings import BaseSettings, SettingsConfigDict


class NemliSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", env_prefix="NEMLI_")

    discord_max_messages: int = 100
    discord_token: str
    openai_api_key: str
    openai_model: str = "gpt-4o-mini"
    openai_system_prompt: str = (
        "Você é um assistente que resume conversas."
        " Você é um assistente de sumarização de texto, você ira receber diversas conversas vindas do discord e deve"
        " sumarizar o conteúdo delas de forma objetiva, sucinta e sem enrolação. Leve em conta os principais pontos"
        " levantados e não invente nenhuma informação extra além do que fora conversado"
    )


settings = NemliSettings()  # type: ignore
