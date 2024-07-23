import nextcord
from nextcord.ext import commands
from openai import OpenAI

from nemli import bot
from nemli.config import settings

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
        channel = interaction.channel  # Here we are getting the channel where the command was called
        # Here we are getting the last 100 messages in the channel
        messages = await channel.history(limit=message_count).flatten()  # type: ignore
        messages_content = "\n".join(
            [f"{msg.author}: {msg.content}" for msg in messages if msg.content and msg.author != bot.user]
        )  # Here we are creating a string with the content of the last 100 messages

        # Here we call the OpenAI API to create a summary of the last 100
        # messages in the channel with the previously created variables
        response = openai_client.chat.completions.create(
            model="gpt-3.5-turbo-16k",
            messages=[
                {
                    "role": "system",
                    "content": "Você é um assistente que resume conversas.",
                },
                {
                    "role": "user",
                    "content": f"Resuma a seguinte conversa em bullet points, sendo detalhista, depois, se relevante, escreva um pequeno parágrafo de conclusão, separando as opiniões de cada usuário em até cinco palavras, lembrando de não estourar um máximo de 1900 caracteres na sua resposta:\n{messages_content}",
                },
            ],
            max_tokens=4000,
            temperature=0.5,
        )

        # Here we are getting the summary from the response and sending it to the user
        summary = response.choices[0].message.content.strip()  # type: ignore
        await interaction.followup.send(f"## Resumo das últimas {message_count} mensagens:\n{summary[:1900]}")
    except Exception:
        await interaction.followup.send(
            "Ocorreu um erro na aplicação. Contate um administrador para resolver o problema."
        )
