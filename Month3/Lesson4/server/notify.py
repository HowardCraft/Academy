import requests
import json
import os
import argparse                    # For parsing command-line options and arguments


# Load config from file
with open('config.json', 'r') as f:
    config = json.load(f)

# ------------- Discord Functions -------------
def send_discord_message(message: str):
    url = config['discord_webhook_url']
    data = {"content": message}
    response = requests.post(url, json=data)

    if response.status_code == 204:
        print("✅ Discord: Message sent successfully!")
    else:
        print("❌ Discord: Failed to send message:", response.text)

def send_discord_image(file_path: str, message: str = ""):
    url = config['discord_webhook_url']
    with open(file_path, 'rb') as f:
        files = {
            'file': (os.path.basename(file_path), f, 'application/octet-stream')
        }
        payload = {
            'payload_json': json.dumps({
                'content': message
            })
        }
        response = requests.post(url, data=payload, files=files)

    if response.status_code in (200, 204):
        print("✅ Discord: Image sent successfully!")
    else:
        print(f"❌ Discord: Failed to send image ({response.status_code}) ->", response.text)

   

# ------------- Telegram Functions -------------
def send_telegram_message(message: str):
    token = config['telegram_bot_token']
    chat_id = config['telegram_chat_id']
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    payload = {'chat_id': chat_id, 'text': message}

    response = requests.post(url, data=payload)

    if response.status_code == 200:
        print("✅ Telegram: Message sent successfully!")
    else:
        print("❌ Telegram: Failed to send message:", response.text)

def send_telegram_image(file_path: str, caption: str = None):
    token = config['telegram_bot_token']
    chat_id = config['telegram_chat_id']
    url = f'https://api.telegram.org/bot{token}/sendPhoto'

    with open(file_path, 'rb') as photo:
        files = {'photo': photo}
        data = {'chat_id': chat_id}
        if caption:
            data['caption'] = caption

        response = requests.post(url, files=files, data=data)

    if response.status_code == 200:
        print("✅ Telegram: Image sent successfully!")
    else:
        print("❌ Telegram: Failed to send image:", response.text)



# ------------- Example Usage -------------
if __name__ == "__main__":

    # This allows users to pass various parameters to the script.
    parser = argparse.ArgumentParser(description="Object Detection and Notification Script")
    # Add an argument for the message to be sent to Discord and Telegram.
    parser.add_argument("--message", type=str, default="👋 Hello from Raspberry Pi 5 with image!",    
                        help="Message to send to Discord and Telegram.")
    # Add an argument for the image file to be sent.
    parser.add_argument("--image", type=str, default="example.jpg",
                        help="Path to the image file to send.")
    # Add an telegram bot action argument.
    parser.add_argument("--telegram_action", type=bool, default=True,
                        help="Action to perform with Telegram bot (send_message or send_image).")
    # Add an argument for the action to perform with the Discord webhook .
    parser.add_argument("--discord_action", type=bool, default=True,
                        help="Action to perform with Discord webhook (send_message or send_image).")


    # Parse the provided arguments.
    args = parser.parse_args()


    if args.telegram_action:
        print("📱 Telegram action is enabled.")
        send_telegram_message(args.message)
        send_telegram_image( args.image, caption="📷 Photo from Pi!"
                            if os.path.exists(args.image) else None)
    
    if args.discord_action:
        print("💬 Discord action is enabled.")
        send_discord_message(args.message)
        send_discord_image( args.image, message="📷 Photo from Pi!"
                            if os.path.exists(args.image) else None)
    

