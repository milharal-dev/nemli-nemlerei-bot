# Initialize bot instance
import nextcord
from nextcord.ext import commands

intents = nextcord.Intents.default()
# Enable message content intent, this is important for the bot to be able to respond to messages
intents.message_content = True
intents.members = True
bot = commands.Bot(
    command_prefix="!",
    intents=intents,
)  # The command_prefix is a placeholder here, we won't be using it
