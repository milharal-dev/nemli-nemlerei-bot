from pydantic_settings import BaseSettings, SettingsConfigDict


class NemliSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8", env_prefix="NEMLI_")

    discord_token: str
    openai_api_key: str
    discord_max_messages: int = 100
    openai_model: str = "gpt-4o-mini"
    openai_temperature: float = 0.3
    openai_system_prompt: str = (
        "Você é um assistente que resume conversas. Para tanto, vai receber mensagens provenientes"
        " do Discord e deve resumir seu conteúdo de forma coerente, coesa e objetiva. Descreva os"
        " principais assuntos. De maneira nenhuma você deve mentir ou inventar fatos, mesmo que"
        " pareçam estar correlacionados, ou sejam com o que poderia ter sido conversado. Sempre"
        " responda respeitando a formatação padrão de arquivos markdown."
    )
    remove_stopwords: bool = True


settings = NemliSettings()  # type: ignore
