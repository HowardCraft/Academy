#!/usr/bin/env python3
"""
transcribe_wav.py

A minimal example that loads a WAV file and transcribes it
to text using Vosk’s offline speech-to-text engine.
"""

import wave
import json
from vosk import Model, KaldiRecognizer

# -----------------------------------------------------------------------------
# 1) Configuration
# -----------------------------------------------------------------------------
# Path to your downloaded Vosk model folder
VOSK_MODEL_PATH = "model"

# Path to the WAV file you want to transcribe
WAV_FILENAME = "test.wav"

# -----------------------------------------------------------------------------
# 2) Load the model
# -----------------------------------------------------------------------------
print(f"Loading Vosk model from '{VOSK_MODEL_PATH}'…")
model = Model(VOSK_MODEL_PATH)

# -----------------------------------------------------------------------------
# 3) Open the WAV file
# -----------------------------------------------------------------------------
wf = wave.open(WAV_FILENAME, "rb")
if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
    raise ValueError(
        "Audio file must be WAV format mono PCM (16-bit). "
        f"Found: channels={wf.getnchannels()}, "
        f"width={wf.getsampwidth()}, "
        f"compression={wf.getcomptype()}"
    )

# Create a recognizer with the sample rate from the file
recognizer = KaldiRecognizer(model, wf.getframerate())

# -----------------------------------------------------------------------------
# 4) Read & transcribe in chunks
# -----------------------------------------------------------------------------
print("Transcribing…")
results = []
while True:
    data = wf.readframes(4000)
    if len(data) == 0:
        break
    if recognizer.AcceptWaveform(data):
        # final result for this chunk
        res = json.loads(recognizer.Result())
        results.append(res.get("text", ""))
    else:
        # partial (you can print partial results if you want)
        # partial = json.loads(recognizer.PartialResult())
        pass

# catch any leftover text
final_res = json.loads(recognizer.FinalResult())
results.append(final_res.get("text", ""))

# -----------------------------------------------------------------------------
# 5) Print the full transcript
# -----------------------------------------------------------------------------
transcript = " ".join(filter(None, results))
print("\n=== Transcript ===")
print(transcript)
