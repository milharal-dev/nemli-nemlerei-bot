import nextcord
from nextcord.ext import commands
from nltk import download as nltk_download

from nemli import bot
from nemli.commands.utility.help import help_command
from nemli.commands.utility.ping import ping_command
from nemli.commands.utility.summarize import summarize_command
from nemli.config import settings


# This function is called when the bot is ready to be used
@bot.event
async def on_ready():
    print(f"Application/Bot online as {bot.user}")
    activity = nextcord.Game("/help")
    await bot.change_presence(status=nextcord.Status.online, activity=activity)


# This function provides error handling for slash commands, specifically for the cooldown feature
@bot.event
async def on_slash_command_error(interaction: nextcord.Interaction, error):
    if isinstance(error, commands.CommandOnCooldown):
        await interaction.response.send_message(f"**Try after {round(error.retry_after, 2)} seconds**")


# This function is responsible for loading the slash commands from the
# commands folder, providing a cleaner and more organized way to
# manage them
def load_commands():
    print("INFO: Loading commands...")

    belted_commands = [
        help_command,
        ping_command,
        summarize_command,
    ]

    for command in belted_commands:
        bot.add_application_command(command)

    print("INFO: Commands loaded successfully!")


# This is the entrypoint for the bot, it will run the bot and load the slash commands
def run():
    nltk_download("punkt")  # Download nltk punkt
    nltk_download("stopwords")  # Download nltk stopwords
    load_commands()
    bot.run(settings.discord_token)
