import nextcord
from nextcord.ext import commands
from nemli.config import settings

intents = nextcord.Intents.default()
intents.message_content = True  # Enable message content intent, this is important for the bot to be able to respond to messages

# Initialize bot instance
bot = commands.Bot(command_prefix="!", intents=intents)  # The command_prefix is a placeholder here, we won't be using it

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

# This function is responsible for loading the slash commands from the commands folder, providing a cleaner and more organized way to manage them
def load_commands():
    print("INFO: Loading commands...")
    
    import nemli.commands.utility.help  
    import nemli.commands.utility.ping  
    import nemli.commands.utility.summarize  
    
    belted_commands = [
        nemli.commands.utility.help.help_command,
        nemli.commands.utility.ping.ping_command,
        nemli.commands.utility.summarize.summarize_command
    ]

    for command in belted_commands:
        bot.add_application_command(command)
    
    print("INFO: Commands loaded successfully!")

# This is the entrypoint for the bot, it will run the bot and load the slash commands
def run():
    load_commands()
    bot.run(settings.discord_token)