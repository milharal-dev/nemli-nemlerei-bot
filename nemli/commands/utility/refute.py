from discord import CategoryChannel, ForumChannel, Message
import nextcord
from nextcord.ext import commands
from loguru import logger

from nemli import bot
from nemli.config import settings
from nemli.nlp.llm.chat import OpenAIBot
from nemli.schemas.messages import ParserDiscordMessages
from nemli.services.messages import parse_discord_messages

openai_client = OpenAIBot()


@bot.slash_command(name="refute")
@commands.cooldown(1, 10, commands.BucketType.channel)
async def refute_command(interaction: nextcord.Interaction):
    logger.debug(f"INFO: Refute command called by: @{interaction.user}")

    # This is a check to make sure that we are only using this function if the user called it correctly,
    # which is to refute a given referenced message
    if not interaction.message or not interaction.message.reference:
        await interaction.response.send_message(
            "Você deve usar este comando em resposta a uma mensagem.", ephemeral=True
        )
        return

    # This is where the magic happens, we retrieve the 'replied to' message here
    message_reference_resolved = interaction.message.reference.resolved
    if message_reference_resolved != Message:
        await interaction.response.send_message("Não foi possível recuperar a mensagem original.", ephemeral=True)
        return

    message_reference: Message = message_reference_resolved  # type: ignore

    logger.debug(f"INFO: Message to be refuted: {message_reference.content}")

    # As always since we're dealing with a complex operation (LLM usage) we need to defer the reply
    # so Discord doesn't shut us off after 3 seconds
    await interaction.response.defer(with_message=True)

    try:
        channel = interaction.channel

        # If somehow the user manages to send a message in a FORUM list of channels
        # or a CATEGORY list of channels (not actual text channels),
        # congratulations.. But Discord still tells us it is possible so :shrug:
        if channel is None or isinstance(channel, (CategoryChannel, ForumChannel)):
            await interaction.followup.send("Este comando não pode ser usado em uma categoria ou fórum.",
                                            ephemeral=True)
            return

        # Here we are creating a string with the content of the last {message_count} messages,
        # this is so the AI has a coherent context to work with,
        # (mostly due to Dark being a chronically online individual who types phrases in four to five messages)
        messages = await channel.history(before=message_reference.created_at, limit=100).flatten()
        messages = [msg for msg in messages if msg.author == message_reference.author]

        # By default we get the last 10 messages starting from the referenced message,
        # but this is configurable through an env var
        messages = messages[: settings.discord.max_messages_to_refute]

        # If by any reason we can't recover a coherent context,
        # we'll not do the function to avoid waste of money and time on the AI
        parsed_discord_messages: ParserDiscordMessages = parse_discord_messages(bot.user, list(reversed(messages)))
        if not parsed_discord_messages.messages:
            await interaction.followup.send("Não há mensagens suficientes para refutar.", ephemeral=True)
            return

        # Magical string manipulation so the AI can be a little less dumb when figuring out the context from the prompt
        messages_content = " ".join([f"{msg.author}: {msg.content}" for msg in parsed_discord_messages.messages or []])

        refuted = openai_client.refute(content=messages_content)

        refuted = (
            "# Há equívocos em sua lógica perfeita! \n\n"
            "Seu argumento é inválido, pois há evidências que refutam sua afirmação.\n\n"
            f"{refuted}"
        )

        await message_reference.reply(refuted)
        await interaction.followup.send(
            f"@{interaction.user} solicitou que uma mensagem seja refutada!", ephemeral=True
        )
    except TimeoutError:
        await interaction.followup.send("Tempo para resposta esgotado.", ephemeral=True)
