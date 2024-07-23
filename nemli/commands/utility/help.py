from nextcord.ext import commands
import nextcord
from nemli import bot


# Same as the ping command, this is just a simple command stating what
# the bot is about and providing the user some guidance, good for
# debugging and boilerplate copy paste
@bot.slash_command(name="help", description="Mensagem de ajuda")
@commands.cooldown(1, 10, commands.BucketType.channel)
async def help_command(interaction: nextcord.Interaction):
    print(f"INFO: The help command has been called by: @{interaction.user}")
    await interaction.response.send_message(
        "Esse bot só tem um propósito: Criar resumos das últimas mensagens enviadas em um canal."
    )
