from typing import Optional

from nextcord import ClientUser
from nextcord import Message as DiscordMessage

from nemli.nlp.messages import clean_up_stopwords
from nemli.schemas.messages import Message, ParserDiscordMessages


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
            message = Message(
                id=msg.id,
                position=i + 1,
                author=f"**{msg.author.global_name or msg.author.name}**",
                content=clean_up_stopwords(message_content),
                jump_url=msg.jump_url,
                created_at=msg.created_at,
            )

        if is_bot_message and message:
            bot_message = message
        elif not is_bot_message and message:
            parsed_messages.append(message)
    # Here we are creating a string with the content of the last N messages
    return ParserDiscordMessages(messages=parsed_messages, bot_message=bot_message)
