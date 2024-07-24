import pytest

from nemli.schemas.messages import Message, ParserDiscordMessages
from nemli.services.messages import parse_discord_messages
from tests.extras.mocks import (
    CREATED_AT,
    mock_discord_client_user,
    mock_discord_message,
)

DEFAULT_OBJ_ID = 100_000

BOT_USER = mock_discord_client_user(obj_id=DEFAULT_OBJ_ID)
DEFAULT_USER = mock_discord_client_user(obj_id=1_000_001)


@pytest.mark.parametrize(
    "user_bot, messages, parsed",
    [
        (None, None, {"messages": None, "bot_message": None}),
        (
            BOT_USER,
            [mock_discord_message(obj_id=DEFAULT_OBJ_ID, author=BOT_USER)],
            {
                "messages": [],
                "bot_message": Message(
                    id=DEFAULT_OBJ_ID,
                    position=1,
                    author="**Mock**",
                    content=f"Message {DEFAULT_OBJ_ID}",
                    jump_url=f"https://discord.com/channels/{DEFAULT_OBJ_ID}/{DEFAULT_OBJ_ID}/{DEFAULT_OBJ_ID}",
                    created_at=CREATED_AT,
                ),
            },
        ),
        (
            mock_discord_client_user(obj_id=BOT_USER),
            [mock_discord_message(obj_id=1_000_001, author=DEFAULT_USER)],
            {
                "messages": [
                    Message(
                        id=1_000_001,
                        position=1,
                        author="**Mock**",
                        content=f"Message {1_000_001}",
                        jump_url=f"https://discord.com/channels/{1_000_001}/{1_000_001}/{1_000_001}",
                        created_at=CREATED_AT,
                    )
                ],
                "bot_message": None,
            },
        ),
    ],
)
def test_parse_discord_messages(user_bot, messages, parsed: dict):
    parsed_discord_messages: ParserDiscordMessages = parse_discord_messages(user_bot=user_bot, messages=messages)
    assert parsed_discord_messages.messages == parsed.get("messages", None)
    assert parsed_discord_messages.bot_message == parsed.get("bot_message", None)
