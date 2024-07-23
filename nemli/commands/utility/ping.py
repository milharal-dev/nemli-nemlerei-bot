import nextcord
from nextcord.ext import commands
from nemli import bot


# This is just a simple ping command to check the bot's latency, good for debugging and boilerplate copy paste
@bot.slash_command(name="ping", description="Checa a latência do bot")
@commands.cooldown(1, 10, commands.BucketType.channel)
async def ping_command(interaction: nextcord.Interaction):
    print(f"INFO: The ping command has been called by: @{interaction.user}")
    await interaction.response.send_message(f"Pong! **{round(bot.latency * 1000, 1)}**ms")
