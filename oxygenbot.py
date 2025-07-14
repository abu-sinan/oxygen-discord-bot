import discord
import requests
import json

# Load API keys from config.json
with open('config.json', 'r') as f:
    config = json.load(f)

GEMINI_API_KEY = config['GEMINI_API_KEY']
DISCORD_BOT_TOKEN = config['DISCORD_BOT_TOKEN']

# Gemini API interaction
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

    for attempt in range(2):  # Retry once if needed
        response = requests.post(url, headers=headers, json=body)
        if response.status_code == 200:
            data = response.json()
            try:
                return data['candidates'][0]['content']['parts'][0]['text']
            except:
                return "Sorry, Gemini couldn't generate a response."
        elif response.status_code == 503:
            continue  # Retry if service unavailable

    return f"Gemini API error: {response.status_code}"

# Discord bot setup
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'OxygenBot is online as {client.user}')

@client.event
async def on_message(message):
    if message.author.bot:
        return  # Ignore bot messages

    # Respond only when mentioned
    if client.user not in message.mentions:
        return

    thinking_message = await message.channel.send("Let me think...")

    reply = ask_gemini(message.content)

    await thinking_message.delete()

    # Split reply into 2000-character chunks
    max_length = 2000
    reply_chunks = [reply[i:i+max_length] for i in range(0, len(reply), max_length)]

    for chunk in reply_chunks:
        embed = discord.Embed(
            title="Response",
            description=chunk,
            color=0x3498DB
        )
        embed.set_footer(text="Powered by Gemini 2.0 Flash")
        await message.channel.send(embed=embed)

client.run(DISCORD_BOT_TOKEN)
