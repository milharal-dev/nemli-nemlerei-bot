from abc import ABC, abstractmethod
from typing import Optional

from openai import OpenAI

from nemli.config import settings


class Bot(ABC):
    def _create_chat(self, messages: list[dict]) -> Optional[str]: ...

    def parse_response(self, message: str) -> str:
        return message.strip().replace("####", "###")

    @abstractmethod
    def summarize(self, prompt: str, messages: str) -> Optional[str]: ...


class OpenAIBot(Bot):
    def __init__(self) -> None:
        super().__init__()
        # Here we are loading the OpenAI API key from .env and creating a client instance for the OpenAI API
        self.client = OpenAI(api_key=settings.openai.api_key)

    def _create_chat(self, messages: list[dict], temperature: float = settings.openai.temperature) -> Optional[str]:
        response = self.client.chat.completions.create(
            model=settings.openai.model,
            messages=messages,  # type: ignore
            max_tokens=4000,
            temperature=temperature,
        )
        if choices := getattr(response, "choices", []):
            return self.parse_response(getattr(getattr(choices[0], "message", None), "content", ""))
        return None

    def summarize(self, prompt: str, content: str) -> Optional[str]:
        messages = [
            {
                "role": "system",
                "content": settings.openai.system_prompt,
            },
            {
                "role": "user",
                "content": f"{prompt}:\n\n{content}",
            },
        ]
        return self._create_chat(messages)
