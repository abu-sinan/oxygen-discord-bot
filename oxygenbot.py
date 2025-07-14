import discord
import requests
import json
import asyncio
import time

# Load API keys from config.json
with open('config.json', 'r') as f:
    config = json.load(f)

GEMINI_API_KEY = config['GEMINI_API_KEY']
DISCORD_BOT_TOKEN = config['DISCORD_BOT_TOKEN']

def ask_gemini(question):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"
    headers = {
        'Content-Type': 'application/json',
        'X-goog-api-key': GEMINI_API_KEY
    }
    body = {
        "contents": [
            {"parts": [{"text": question}]}
        ]
    }

    response = requests.post(url, headers=headers, json=body)

    if response.status_code == 200:
        data = response.json()
        try:
            return data['candidates'][0]['content']['parts'][0]['text']
        except:
            return "Sorry, Gemini couldn't generate a response."
    else:
        return f"Gemini API error: {response.status_code}"

# Discord Bot Setup
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Cooldown tracking dict: user_id -> last message timestamp
user_cooldowns = {}

@client.event
async def on_ready():
    print(f'OxygenBot is online as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if client.user not in message.mentions:
        return

    now = time.time()
    cooldown = 10  # seconds cooldown per user
    last_time = user_cooldowns.get(message.author.id, 0)

    if now - last_time < cooldown:
        await message.channel.send(f"Please wait a bit before asking again, {message.author.mention}.")
        return

    user_cooldowns[message.author.id] = now

    thinking_message = await message.channel.send("Let me think...")

    reply = ask_gemini(message.content)

    await thinking_message.delete()

    # Split long replies into 2000-character chunks
    max_length = 2000
    reply_chunks = [reply[i:i+max_length] for i in range(0, len(reply), max_length)]

    max_chunks = 5  # limit number of chunks sent to avoid spam

    for chunk in reply_chunks[:max_chunks]:
        embed = discord.Embed(
            title="OxygenBot AI Response",
            description=chunk,
            color=0x3498DB
        )
        embed.set_footer(text="Powered by Gemini 2.0 Flash")
        await message.channel.send(embed=embed)
        await asyncio.sleep(1)  # pause 1 second between messages

    if len(reply_chunks) > max_chunks:
        await message.channel.send(f"...and more response not shown to avoid spam.")

client.run(DISCORD_BOT_TOKEN)