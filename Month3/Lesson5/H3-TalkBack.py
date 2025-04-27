#!/usr/bin/env python3
"""
synth_to_file_subprocess.py

Uses espeak-ng + subprocess to write synthesized speech into a WAV file.
"""

import subprocess

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
    sample_text = "Hello, this is a test of writing speech to a file."
    synth_to_file(sample_text, "test.wav", voice="en-us", speed=150, pitch=70)

    # (Optional) play it back to verify
    print("Playing back test.wav …")
    subprocess.run(["aplay", "test.wav"], check=True)
