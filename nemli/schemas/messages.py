from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass(frozen=True, slots=True)
class Message:
    id: int
    position: int
    author: str
    content: str
    jump_url: str
    created_at: datetime


@dataclass(frozen=True, slots=True)
class ParserDiscordMessages:
    messages: Optional[list[Message]]
    bot_message: Optional[Message]
