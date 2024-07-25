from typing import Optional

from loguru import logger
from nextcord import ClientUser
from nextcord import Message as DiscordMessage

from nemli.config import settings
from nemli.nlp.messages import clean_up_stopwords
from nemli.schemas.messages import Message, ParserDiscordMessages


def is_summary_link_message(message_content: str) -> bool:
    logger.debug(message_content)
    return message_content.lower().startswith("nemli:")


def parse_discord_messages(
    user_bot: Optional[ClientUser] = None,
    messages: Optional[list[DiscordMessage]] = None,
) -> ParserDiscordMessages:
    if not (user_bot and messages):
        return ParserDiscordMessages(messages=None, bot_message=None)

    parsed_messages, bot_message = [], None
    for i, msg in enumerate(messages):
        is_bot_message = msg.author == user_bot

        message = None
        if message_content := msg.content:
            content = clean_up_stopwords(message_content) if settings.remove_stopwords else message_content
            message = Message(
                id=msg.id,
                position=i + 1,
                author=f"**{msg.author.global_name or msg.author.name}**",
                content=content,
                jump_url=msg.jump_url,
                created_at=msg.created_at,
            )

        if is_bot_message and message and not is_summary_link_message(message_content):
            bot_message = message
        elif not is_bot_message and message:
            parsed_messages.append(message)
    # Here we are creating a string with the content of the last N messages
    return ParserDiscordMessages(messages=parsed_messages, bot_message=bot_message)
