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
   # 1) List your USB mic (and any others)
   list_input_devices()

   # 3) Ask how many seconds to record
   duration = float(input("Enter recording duration in seconds (e.g. 5): "))


   # 4) output filename
   filename = "test.wav"


   # 5) Set audio parameters
   SAMPLERATE = 16000   # 16 kHz is typical for speech
   CHANNELS   = 1       # mono


   # 6) Do the recording
   audio_data = record_audio(duration, SAMPLERATE, CHANNELS)


   # 7) Save to WAV
   sf.write(filename, audio_data, SAMPLERATE)
   print(f"Saved recording to '{filename}'\n")


   # # 8) (Optional) Playback
   # if input("Play it back now? (y/N): ").lower().startswith('y'):
   #     print("→ Playing back…")
   #     data, fs = sf.read(filename, dtype='int16')
   #     sd.play(data, fs)
   #     sd.wait()
   #     print("→ Playback finished.")


if __name__ == "__main__":
   main()


