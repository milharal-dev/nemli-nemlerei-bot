from datetime import datetime
from random import randint
from unittest.mock import MagicMock

from nextcord import ClientUser
from nextcord import Message as DiscordMessage

CREATED_AT = datetime.now()


def mock_discord_guild(obj_id: int = randint(1_000_000, 10_000_000)):
    mock = MagicMock()
    mock.id = obj_id
    mock.get_member = lambda user_id: mock_discord_client_user(1_000_001)
    return mock


def mock_discord_client_user(obj_id: int = randint(1_000_000, 10_000_000)):
    mock = MagicMock(spec=ClientUser)
    mock.id = obj_id
    mock.nick = "Mock"
    mock.global_name = "Mock"
    return mock


def mock_discord_message(obj_id: int = randint(1_000_000, 10_000_000), author=None):
    mock = MagicMock(spec=DiscordMessage)
    mock.id = obj_id
    mock.author = author
    mock.guild = mock_discord_guild(obj_id=obj_id)
    mock.content = f"Message {obj_id}"
    mock.jump_url = f"https://discord.com/channels/{obj_id}/{obj_id}/{obj_id}"
    mock.created_at = CREATED_AT
    return mock
