# Initialize bot instance
from nextcord.ext import commands
import nextcord

intents = nextcord.Intents.default()
# Enable message content intent, this is important for the bot to be able to respond to messages
intents.message_content = True
bot = commands.Bot(
    command_prefix="!",
    intents=intents,
)  # The command_prefix is a placeholder here, we won't be using it
