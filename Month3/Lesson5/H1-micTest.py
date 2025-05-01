#!/usr/bin/env python3
"""
A minimal script to verify your USB microphone on Raspberry Pi:
 1. Lists input devices
 2. Records for a user-specified duration
 3. Saves the audio to a WAV file
 4. Optionally plays it back
"""


import sounddevice as sd
import soundfile as sf
import argparse 
from server.notify import send_telegram_audio, send_discord_audio

def list_input_devices():
   print("== Available audio INPUT devices ==")
   # Show only capture (input) devices
   print(sd.query_devices(kind='input'))


def record_audio(duration, samplerate, channels):
   """
   Records `duration` seconds from `device_index` at given samplerate/channels.
   Returns a NumPy array of int16 samples.
   """
   print(f"\n→ Recording {duration:.1f}s")
   audio = sd.rec(
       int(duration * samplerate),
       samplerate=samplerate,
       channels=channels,
       dtype='int16',
   )
   sd.wait()  # block until recording is done
   print("Recording completed.")
   return audio


def main():
    # This allows users to pass various parameters to the script.
   parser = argparse.ArgumentParser(description="Audio Script")
       # Add an telegram bot action argument.
   parser.add_argument("--telegram_action", type=bool, default=True,
                        help="Action to perform with Telegram bot (send_telegram_audio).")
    # Add an argument for the action to perform with the Discord webhook .
   parser.add_argument("--discord_action", type=bool, default=True,
                        help="Action to perform with Discord webhook (send_discord_audio).")
   parser.add_argument(
        "--duration", "-d",
        type=float,
        default=5.0,
        help="Recording duration in seconds (e.g. 5.0)"
    )
   parser.add_argument(
        "--filename", "-o",
        type=str,
        default="test.wav",
        help="Output WAV filename"
    )
   parser.add_argument(
        "--samplerate", "-r",
        type=int,
        default=16000,
        help="Sample rate in Hz (default: 16000)"
    )
   parser.add_argument(
        "--channels", "-c",
        type=int,
        choices=[1, 2],
        default=1,
        help="Number of channels: 1=mono, 2=stereo"
    )
       # Parse the provided arguments.
   args = parser.parse_args()
   
   # 1) List your USB mic (and any others)
   list_input_devices()

   # 6) Do the recording
   audio_data = record_audio(args.duration, args.samplerate, args.channels)


   # 7) Save to WAV
   sf.write(args.filename, audio_data, args.samplerate)
   print(f"Saved recording to '{args.filename}'\n")


   # # 8) (Optional) Send to Telegram
   if args.telegram_action:
         send_telegram_audio(args.filename, caption="Audio recording")
         print("Telegram action triggered.") 
   # # 9) (Optional) Send to Discord
   if args.discord_action:
         send_discord_audio(args.filename, meesage="Audio recording")
         print("Discord action triggered.")


if __name__ == "__main__":
   main()


