#!/usr/bin/env python3
"""
command_matcher.py

Given a live transcript from Vosk, find which predefined command
the user meant, using fuzzy matching (difflib).
"""

import difflib

# 1) Define your set of valid commands and the functions they map to:
def cmd_turn_on_light():
    print("💡 Turning light ON")

def cmd_turn_off_light():
    print("💡 Turning light OFF")

def cmd_start_recording():
    print("🎤 Starting recording…")

def cmd_stop_recording():
    print("🎤 Stopping recording!")

COMMANDS = {
    "turn on the light":    cmd_turn_on_light,
    "turn off the light":   cmd_turn_off_light,
    "start recording":      cmd_start_recording,
    "stop recording":       cmd_stop_recording,
}

# 2) Helper to pick the closest command
def match_command(transcript: str, commands: dict, cutoff: float = 0.6):
    """
    Returns the best matching command key, or None if below cutoff.
    
    :param transcript: the raw text you got from Vosk
    :param commands:    dict mapping command_text -> handler
    :param cutoff:      similarity threshold (0–1)
    """
    # get_close_matches returns a list of keys with score ≥ cutoff
    matches = difflib.get_close_matches(
        transcript.lower(),
        commands.keys(),
        n=1,
        cutoff=cutoff
    )
    return matches[0] if matches else None

# 3) Example loop: pretend we’ve just got this transcript
if __name__ == "__main__":
    while True:
        raw = input("\nSimulate transcript> ")  # replace with your recognizer.Result()["text"]
        if not raw:
            print("Exiting.")
            break

        cmd_text = match_command(raw, COMMANDS, cutoff=0.6)
        if cmd_text:
            print(f"→ Matched command: '{cmd_text}'")
            COMMANDS[cmd_text]()  # call the handler
        else:
            print("→ Sorry, I didn't understand that command.")
