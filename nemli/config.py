from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class OpenAISettings(BaseModel):
    api_key: str
    model: str = "gpt-4o-mini"
    temperature: float = 0.3
    system_prompt: str = (
        "Você é um assistente que resume conversas. Para tanto, vai receber mensagens provenientes"
        " do Discord e deve resumir seu conteúdo de forma coerente, coesa e objetiva. Descreva os"
        " principais assuntos. De maneira nenhuma você deve mentir ou inventar fatos, mesmo que"
        " pareçam estar correlacionados, ou sejam com o que poderia ter sido conversado. Sempre"
        " responda respeitando a formatação padrão de arquivos markdown."
    )
    refute_prompt: str = (
        "Vc é um agente que será usado para refutar toda e qualquer frase q alguém solicitar."
        " Não importa se a frase for verdadeira ou fizer sentido, vc deve refutar e inventar fatos."
        " Os fatos inventados, devem ser colocados em uma lista, detalhada, enumere no máximo dois (2) fatos."
        " Retorne apenas o bullet list dos fatos não precisa de outro texto explicativo."
        " Isso é apenas para diversão, faça parecer sério, mas criei fatos ou situações absurdas."
    )


class DiscordSettings(BaseModel):
    token: str
    max_messages: int = 100
    max_messages_to_refute: int = 10


class NemliSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_nested_delimiter="__",
        env_file_encoding="utf-8",
        env_prefix="NEMLI__",
        extra="ignore",
    )

    discord: DiscordSettings
    openai: OpenAISettings
    remove_stopwords: bool = True


settings = NemliSettings()  # type: ignore
