![Oxygen Bot](https://github.com/abu-sinan/oxygenbot/blob/main/assets/discord_bot.png)
# 🤖 OxygenBot

OxygenBot is a lightweight Discord chatbot powered by Google Gemini 2.0 Flash API. It responds to messages where it's mentioned, providing AI-generated answers directly in Discord.

---

## 🎯 Features

- 💬 Replies only when mentioned (e.g., `@OxygenBot Who are you?`).
- 📖 Long responses are automatically split across multiple messages.
- 📊 Uses clean Discord embeds for professional replies.
- 🔐 API keys secured via external config file.

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/abu-sinan/oxygenbot.git
cd oxygenbot
```

### 2️⃣ Install Dependencies

```bash
pip install discord.py requests
```

### 3️⃣ Create config.json

In the project folder, create a file named `config.json`:

```json
{
    "GEMINI_API_KEY": "YOUR_GEMINI_API_KEY",
    "DISCORD_BOT_TOKEN": "YOUR_DISCORD_BOT_TOKEN"
}
```

### 4️⃣ Run OxygenBot

```bash
python oxygenbot.py
```

OxygenBot will display a message in the terminal when it’s online.

---

## ⚠️ Security Notes

Never share your real API keys publicly.

Ensure `config.json` is listed in your `.gitignore` to prevent uploading sensitive data.

---

## 📄 Example Usage

In Discord:

`@OxygenBot How does AI work?`

OxygenBot:

Shows "Let me think..."

Replies with AI-generated answer using Gemini 2.0 Flash.

---

## 🛠️ Planned Features

Optional response logging.

Web dashboard.

Multi-channel support.

Slash command integration.

---

## 📃 License

MIT License