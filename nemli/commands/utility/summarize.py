import nextcord
from nextcord.ext import commands
from openai import OpenAI

from nemli import bot
from nemli.config import settings
from nemli.schemas.messages import ParserDiscordMessages
from nemli.services.messages import parse_discord_messages

# Here we are loading the OpenAI API key from .env and creating a client instance for the OpenAI API
openai_client = OpenAI(api_key=settings.openai_api_key)


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
        default=settings.discord_max_messages,
    ),
):
    print(f"INFO: The summarize command has been called by: @{interaction.user}")

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
                (
                    "Um resumo já foi criado recentemente, e se encontra em "
                    f"{message_count - bot_message.position}/{message_count}:"
                    f"[Último resumo]({bot_message.jump_url})"
                )
            )
            return

        messages_content = " ".join([f"{msg.author}: {msg.content}" for msg in parsed_discord_messages.messages or []])

        # Here we call the OpenAI API to create a summary of the last {message_count}
        # messages in the channel with the previously created variables
        response = openai_client.chat.completions.create(
            model=settings.openai_model,
            messages=[
                {
                    "role": "system",
                    "content": settings.openai_system_prompt,
                },
                {
                    "role": "user",
                    "content": (
                        "Resuma a seguinte conversa por assuntos, agrupando assuntos que forem similares o "
                        "máximo possível e relacionado os assuntos com os usuários que participem da discussão:\n\n"
                        f"{messages_content}"
                    ),
                },
            ],
            max_tokens=4000,
            temperature=0.5,
        )

        # Here we are getting the summary from the response and sending it to the user
        summary = response.choices[0].message.content.strip()  # type: ignore
        response_list = response_to_list(summary, header=f"Resumo das últimas {message_count} mensagens")
        for resp in response_list:
            await interaction.followup.send(resp)
    except Exception:
        await interaction.followup.send(
            "Ocorreu um erro na aplicação. Contate um administrador para resolver o problema."
        )


def response_to_list(summary, header, counter=0):
    counter += 1
    msg_char_lim = 1900
    msg_header = header + f", parte {counter}:\n"
    l_marker = "\n"

    # Small responses
    if len(summary) < msg_char_lim:
        return [summary]

    # Line breaks
    line_positions = [i for i, sub in enumerate(summary[: -len(l_marker)]) if sub == l_marker]
    line_break = (
        (
            max([t for t in line_positions if t < msg_char_lim])
            if any(map(lambda x: x < msg_char_lim, line_positions))
            else None
        )
        if l_marker in summary
        else None
    )

    # Big responses
    if line_break:
        return [msg_header + summary[:line_break], *response_to_list(summary[line_break:], header, counter)]
    else:
        return [msg_header + summary[:msg_char_lim], *response_to_list(summary[msg_char_lim:], header, counter)]
