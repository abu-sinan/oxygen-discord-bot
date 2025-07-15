![Oxygen Discord Bot](https://github.com/abu-sinan/oxygen-discord-bot/blob/main/assets/discord_bot.png)
# 🫧 Oxygen - Discord AI Bot (Gemini API)

Oxygen is a lightweight Discord bot powered by Google's Gemini AI. It listens for mentions in messages, forwards your question to Gemini, and replies with an AI-generated response inside a clean embed.

---

## ✨ Features

- Uses **Google Gemini 2.0 Flash** model.

- Replies only when mentioned (no spam).

- Shows Discord’s native **typing indicator** while thinking.

- Answers are returned inside a **styled embed**.

- Automatically trims long replies to fit Discord’s limits.

---

## 📦 Requirements

- Python 3.9+

- `discord.py`

- `requests`

- `python-dotenv`

---

## ⚙️ Installation

### 1. Clone the project:

```bash
git clone https://github.com/abu-sinan/oxygen-discord-bot.git
cd oxygen-discord-bot
```

### 2. Install dependencies:

```bash
pip install -r requirements.txt
```

### 3. Set up .env file:

Create a `.env` file in the project directory:

```.env
DISCORD_TOKEN=YOUR_DISCORD_BOT_TOKEN
GEMINI_API_KEY=YOUR_GEMINI_API_KEY
```

### 4. Run the bot:

```bash
python bot.py
```

---

## 📋 Usage

- Mention Oxygen in any channel it has access to, followed by your question:


`@Oxygen How does AI work?`

- Oxygen will reply using the Gemini API.

---

## 🛠️ Configuration

`MAX_EMBED_LENGTH` inside `bot.py` limits message size to avoid Discord embed errors. Default: 4000 characters.

---

## 📑 Example Reply

> @Oxygen What is AI?



Oxygen replies with an embed:

```
Artificial intelligence (AI) is the simulation of human intelligence processes by machines...
```

---

## 🤖 Tech Stack

- Python

- discord.py

- Google Generative Language API (Gemini)

- dotenv

---

## 📃 License

MIT [License](https://github.com/abu-sinan/oxygen-discord-bot/blob/main/LICENSE)