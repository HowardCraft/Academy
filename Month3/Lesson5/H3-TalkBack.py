#!/usr/bin/env python3
"""
synth_to_file_subprocess.py

Uses espeak-ng + subprocess to write synthesized speech into a WAV file.
"""

import subprocess
import argparse 
from server.notify import send_telegram_audio, send_discord_audio

def synth_to_file(text: str,
                  filename: str = "output.wav",
                  voice: str = "en-us",
                  speed: int = 175,
                  pitch: int = 50) -> None:
    """
    Synthesizes `text` and writes the resulting WAV bytes to `filename`.

    :param text:     The text you want spoken.
    :param filename: The path to the output WAV file.
    :param voice:    eSpeak-NG voice identifier (e.g. "en", "en-us", "es").
    :param speed:    Words per minute (80–450).
    :param pitch:    Pitch 0–99 (default 50).
    """
    # Build the espeak-ng command:
    cmd = [
        "espeak-ng",
        "-v", voice,
        "-s", str(speed),
        "-p", str(pitch),
        "--stdout"           # emit WAV data to stdout
    ]

    # Open the file in binary-write mode and run espeak-ng,
    # sending `text` via stdin and capturing stdout in the file.
    with open(filename, "wb") as wav_file:
        subprocess.run(
            cmd,
            input=text.encode("utf-8"),   # feed text into espeak-ng
            stdout=wav_file,              # write WAV bytes here
            check=True
        )
    print(f"[+] Synthesis complete: '{filename}'")

if __name__ == "__main__":
    # Example usage
    parser = argparse.ArgumentParser(description="Audio Script")
       # Add an telegram bot action argument.
    parser.add_argument("--telegram_action", type=bool, default=True,
                        help="Action to perform with Telegram bot (send_telegram_audio).")
    # Add an argument for the action to perform with the Discord webhook .
    parser.add_argument("--discord_action", type=bool, default=True,
                        help="Action to perform with Discord webhook (send_discord_audio).")
    parser.add_argument(
        "--filename", "-o",
        type=str,
        default="test.wav",
        help="Output WAV filename"
    )
    args = parser.parse_args()
    sample_text = "Hello, this is a test of writing speech to a file."
    synth_to_file(sample_text, "test.wav", voice="en-us", speed=150, pitch=70)

    # (Optional) play it back to verify
    print("Playing back test.wav …")
    subprocess.run(["aplay", "test.wav"], check=True)
    
    # (Optional) Send to Telegram
    if args.telegram_action:
         send_telegram_audio(args.filename, caption="Audio recording")
         print("Telegram action triggered.") 
    # (Optional) Send to Discord
    if args.discord_action:
         send_discord_audio(args.filename, message="Audio recording")
         print("Discord action triggered.")
