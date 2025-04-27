# 🔔 Webhook Setup Guide for Telegram & Discord

This guide will walk you through setting up webhooks for **Telegram** and **Discord** so you can send messages or images from a Python script (e.g., on a Raspberry Pi).

---

## 📦 Prerequisites

- Python installed
- Internet access
- `requests` library (install with `pip install requests`)

---

## 🔗 Discord Webhook Setup

### 1. Create a Webhook

1. Open Discord and go to your **server**.
2. Click the **gear icon** next to the channel you want to use.
3. Go to **Integrations > Webhooks**.
4. Click **“New Webhook”**.
5. Name your webhook (e.g., `PiNotifier`), select the target channel, and click **Copy Webhook URL**.

This URL will look like:

```
https://discord.com/api/webhooks/1234567890/ABCDEF...
```

Save this — it's your **Discord Webhook URL**.

---

## 📬 Telegram Bot Webhook Setup

### 1. Create a Telegram Bot

1. Open Telegram and search for **@BotFather**.
2. Start a chat and type `/newbot`.
3. Follow the prompts:
   - Give your bot a name (e.g., `Pi Notifier Bot`)
   - Choose a username (must end in `bot`, like `pi_notifier_bot`)
4. You’ll get a **bot token** like:

```
123456789:ABCdefGHIjklMNOpQRstuvWXyZ
```

Save this — it’s your **Telegram Bot Token**.

---

### 2. Get Your Telegram Chat ID

You can use a helper bot like [@userinfobot](https://t.me/userinfobot):

1. Start the bot.
2. It will show your **chat ID** (usually a number like `60537697`).


---

## ✅ Testing with Python

Install requests if needed by running install.sh:

```bash
./install.sh
```

## Add your tokens to the config.json 

```
{
    "discord_webhook_url": " https://discord.com/api/...",
    "telegram_bot_token": "78.....",
    "telegram_chat_id": "23.."
}

```
## 💡 Tips

- Keep tokens secret! Don't share them publicly.
---

## Test

For test you need to run notify.py file

```
python3 notify.py

```

You must recive image and text messge in both Discord and Telegram


# Security Cam:

Run tflite_object_detection_live_security_cam.py 

python3 tflite_object_detection_live_security_cam.py

By default live camera is activated.
New configuration are reusing codes from notify.py 


## 🙋‍♂️ Questions?

Ask your instructor or search the Telegram/Discord API docs for more!

Happy hacking! 🚀
