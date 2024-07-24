from datetime import datetime
from random import randint
from unittest.mock import MagicMock

from nextcord import ClientUser
from nextcord import Message as DiscordMessage

CREATED_AT = datetime.now()


def mock_discord_client_user(obj_id: int = randint(1_000_000, 10_000_000)):
    mock = MagicMock(spec=ClientUser)
    mock.id = obj_id
    mock.global_name = "Mock"
    return mock


def mock_discord_message(obj_id: int = randint(1_000_000, 10_000_000), author=None):
    mock = MagicMock(spec=DiscordMessage)
    mock.id = obj_id
    mock.author = author
    mock.content = f"Message {obj_id}"
    mock.jump_url = f"https://discord.com/channels/{obj_id}/{obj_id}/{obj_id}"
    mock.created_at = CREATED_AT
    return mock
