import nextcord
from loguru import logger
from nextcord.ext import commands

from nemli import bot
from nemli.config import settings
from nemli.nlp.llm.chat import OpenAIBot
from nemli.schemas.messages import ParserDiscordMessages
from nemli.schemas.prompt_style import prompt_types
from nemli.services.messages import parse_discord_messages

openai_client = OpenAIBot()


# This is the slash command that will be used to create a summary of
# the last 20 to 1000 messages in the channel, the main feature of this bot
@bot.slash_command(name="summarize", description="Cria um resumo das últimas 100 mensagens no canal")
@commands.cooldown(1, 10, commands.BucketType.channel)
async def summarize_command(
    interaction: nextcord.Interaction,
    message_count: int = nextcord.SlashOption(
        name="mensagens",
        description="Número de mensagens a serem resumidas (20-1000)",
        required=False,
        min_value=20,
        max_value=1000,
        default=settings.discord.max_messages,
    ),
    prompt_type: str = nextcord.SlashOption(
        name="tipo_prompt",
        description="Tipo de prompt a ser usado",
        required=False,
        choices=prompt_types,
    ),
):
    logger.debug(f"INFO: The summarize command has been called by: @{interaction.user}")

    # We defer the response so we avoid timeout errors due to AI processing which could take longer than three seconds
    await interaction.response.defer(with_message=True)

    try:
        # Here we are getting the channel where the command was called
        channel = interaction.channel
        # Here we are getting the last {message_count} messages in the channel
        messages = await channel.history(limit=message_count).flatten()  # type: ignore

        # Here we are creating a string with the content of the last {message_count} messages
        parsed_discord_messages: ParserDiscordMessages = parse_discord_messages(bot.user, list(reversed(messages)))
        if not (parsed_discord_messages.messages):
            await interaction.followup.send("Não há mensagens suficientes para criar um resumo.")
            return

        # If we have bot message resume in the last {message_count} messages, we will not create a new summary
        if bot_message := parsed_discord_messages.bot_message:
            await interaction.followup.send(
                "Nemli: um resumo já foi criado recentemente, e se encontra em "
                f"{message_count - bot_message.position}/{message_count}:\n\n"
                f"[Último resumo]({bot_message.jump_url})"
            )
            return

        messages_content = " ".join([f"{msg.author}: {msg.content}" for msg in parsed_discord_messages.messages or []])

        user_prompt = prompt_types.get(prompt_type, prompt_types.get("padrão", ""))
        prompt_type = prompt_type or "padrão"

        # Here we call the OpenAI API to create a summary of the last {message_count}
        # messages in the channel with the previously created variables
        summary = openai_client.summarize(user_prompt, messages_content)
        if not summary:
            await interaction.followup.send("Não foi possível criar um resumo devido a erro de retorno da API.")
            return

        message_count_url: str = f"{message_count}"
        if first_message := parsed_discord_messages.messages[0]:
            message_count_url = f"[{message_count}]({first_message.jump_url})"

        # Here we are getting the summary from the response and sending it to the user
        header = f"# Resumo das últimas {message_count_url} mensagens (tipo: {prompt_type})"
        response_list = response_to_list(summary, header=header)
        for resp in response_list:
            await interaction.followup.send(resp)
    except nextcord.errors.Forbidden as e:
        logger.exception(e)
        await interaction.followup.send(
            "Esse bot experimental não pode ser usado nesse canal, "
            "é reservado aos desenvolvedores. Tente usar o @Nemli Nemlerei."
        )
    except Exception as e:
        logger.exception(e)
        await interaction.followup.send(
            "Ocorreu um erro na aplicação. Contate um administrador para resolver o problema."
        )


def response_to_list(summary, header, counter=0, msg_char_lim=1950):
    counter += 1
    msg_header = header + f", parte {counter}:\n" if header else ""

    def get_break(marker):
        positions = [
            i
            for i, sub in enumerate([summary[j:j + len(marker)] for j in range(len(summary) - -len(marker))])
            if sub == marker
        ]
        return (
            (
                max([t for t in positions if t < (msg_char_lim - len(msg_header))])
                if any(map(lambda x: x < (msg_char_lim - len(msg_header)), positions))
                else None
            )
            if marker in summary
            else None
        )

    # Small responses
    if len(summary) < (msg_char_lim - len(msg_header)):
        return [msg_header + summary]

    # Big responses
    limit = get_break("\n#") or get_break("\n") or msg_char_lim
    return [
        msg_header + summary[:limit],
        *response_to_list(summary[limit:], header, counter, msg_char_lim),
    ]
