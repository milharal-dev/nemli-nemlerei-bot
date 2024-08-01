import nextcord

from nemli import bot
from nemli.config import settings
from nemli.nlp.llm.chat import OpenAIBot
from nemli.schemas.messages import ParserDiscordMessages
from nemli.services.messages import parse_discord_messages

openai_client = OpenAIBot()


@bot.message_command(name="refute")
async def refute_command(interaction: nextcord.Interaction, reference_message: nextcord.Message):
    print(f"INFO: The summarize command has been called by: @{interaction.user}")
    print(f"Refute message: {reference_message.content}")

    # We defer the response so we avoid timeout errors due to AI processing which could take longer than three seconds
    await interaction.response.defer(with_message=True)

    try:
        # Here we are getting the channel where the command was called
        channel = interaction.channel

        # Fetch messages from the channel, after the reference message
        messages = await channel.history(before=reference_message.created_at, limit=100).flatten()  # type: ignore
        # Filter messages to only include those from the specified user
        messages = [msg for msg in messages if msg.author == reference_message.author]
        # Get the last 10 messages from the user
        messages = messages[: settings.discord.max_messages_to_refute]

        # Here we are creating a string with the content of the last {message_count} messages
        parsed_discord_messages: ParserDiscordMessages = parse_discord_messages(bot.user, list(reversed(messages)))
        if not (parsed_discord_messages.messages):
            await interaction.followup.send("Não há mensagens suficientes para refutar.")
            return

        messages_content = " ".join([f"{msg.author}: {msg.content}" for msg in parsed_discord_messages.messages or []])
        refuted = openai_client.refute(content=messages_content)

        refuted = (
            "# Há equívocos em sua lógica perfeita! \n\n"
            "Seu argumento é inválido, pois há evidências que refutam sua afirmação.\n\n"
            f"{refuted}"
        )
        await reference_message.reply(refuted)
        await interaction.followup.send(
            f"@{interaction.user} soliticou que uma mensagem seja refutada!", ephemeral=True
        )
    except TimeoutError:
        await interaction.followup.send("Tempo para resposta esgotado.", ephemeral=True)
