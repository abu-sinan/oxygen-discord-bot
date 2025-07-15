import discord
import os
import requests
import json
import asyncio
from dotenv import load_dotenv
import logging

logging.basicConfig(level=logging.ERROR)

# Load API keys from .env file
load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

# Gemini API endpoint
GEMINI_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"

# Discord bot setup
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

client = discord.Client(intents=intents)

MAX_EMBED_LENGTH = 4000  # Keep safely under Discord's 6000 limit

def ask_gemini(prompt):
    headers = {
        "Content-Type": "application/json",
        "X-goog-api-key": GEMINI_API_KEY
    }
    body = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    try:
        response = requests.post(GEMINI_URL, headers=headers, data=json.dumps(body))
        if response.status_code == 200:
            data = response.json()
            return data['candidates'][0]['content']['parts'][0]['text']
        else:
            logging.error(f"API Error {response.status_code}: {response.text}")
            return None
    except Exception as e:
        logging.error(f"Exception calling Gemini API: {e}")
        return None

@client.event
async def on_ready():
    print(f'✅ Oxygen is online as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return

    if client.user in message.mentions:
        prompt = message.content.replace(f'<@{client.user.id}>', '').strip()

        if prompt == "":
            await message.channel.send("❓ Mention me with a question!")
            return

        async with message.channel.typing():
            reply = await asyncio.to_thread(ask_gemini, prompt)

        if reply:
            if len(reply) > MAX_EMBED_LENGTH:
                reply = reply[:MAX_EMBED_LENGTH] + "\n\n*Reply truncated due to Discord limits.*"

            embed = discord.Embed(
                description=reply,
                color=discord.Color.teal()
            )
            embed.set_footer(text="Powered by Oxygen AI")
            await message.reply(embed=embed)
        else:
            await message.reply("⚠️ API Error: Could not get a reply.")

client.run(DISCORD_TOKEN)