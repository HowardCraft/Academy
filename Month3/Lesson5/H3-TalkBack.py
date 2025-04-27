from espeakng import ESpeakNG

esng = ESpeakNG()
esng.voice = "en-us"
esng.speed = 175
esng.pitch = 50

# Speak immediately
esng.say("Hello from py-espeak-ng!")

# Synthesize to WAV array
wav_bytes = esng.synth("This returns raw WAV data.")
with open("wrapper_output.wav", "wb") as f:
    f.write(wav_bytes)
