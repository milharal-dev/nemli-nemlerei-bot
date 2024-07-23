import os
import nextcord
from openai import OpenAI
from nextcord.ext import commands
from nemli.main import bot

# Here we are loading the OpenAI API key from .env and creating a client instance for the OpenAI API
OPENAI_API_KEY = os.getenv('NEMLI__OPENAI__API__KEY')
client = OpenAI(api_key=OPENAI_API_KEY)

# This is the slash command that will be used to create a summary of the last 100 messages in the channel, the main feature of this bot
@bot.slash_command(
    name="summarize",
    description="Cria um resumo das últimas 100 mensagens no canal"
)
@commands.cooldown(1, 10, commands.BucketType.channel)
async def summarize_command(interaction: nextcord.Interaction, message_count: int = nextcord.SlashOption(
            name="mensagens",
            description="Número de mensagens a serem resumidas (20-500)",
            required=False,
            min_value=20,
            max_value=500,
            default=100
        )):
    print(f'INFO: The summarize command has been called by: @{interaction.user}')
    channel = interaction.channel # Here we are getting the channel where the command was called
    messages = await channel.history(limit=message_count).flatten() # Here we are getting the last 100 messages in the channel
    messages_content = "\n".join([f"{msg.author}: {msg.content}" for msg in messages if msg.content]) # Here we are creating a string with the content of the last 100 messages

    # Here we call the OpenAI API to create a summary of the last 100 messages in the channel with the previously created variables
    response = client.chat.completions.create(model="gpt-3.5-turbo-16k",
    messages=[
        {"role": "system", "content": "Você é um assistente que resume conversas."},
        {"role": "user", "content": f"Resuma a seguinte conversa:\n{messages_content}"}
    ],
    max_tokens=1000,
    temperature=0.5)

    # Here we are getting the summary from the response and sending it to the user
    summary = response.choices[0].message.content.strip()
    await interaction.response.send_message(f"## Resumo das últimas {message_count} mensagens:\n{summary}")