
import sounddevice as sd
import soundfile as sf
import wave
import json
from vosk import Model, KaldiRecognizer




# Path to the WAV file you want to transcribe
WAV_FILENAME = "test.wav"

def record_audio(duration, samplerate, channels,filename):
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
    sf.write(filename, audio, samplerate)
    return audio



def transcribe_audio(WAV_FILENAME):
    wf = wave.open(WAV_FILENAME, "rb")
    if wf.getnchannels() != 1 or wf.getsampwidth() != 2 or wf.getcomptype() != "NONE":
        raise ValueError(
            "Audio file must be WAV format mono PCM (16-bit). "
            f"Found: channels={wf.getnchannels()}, "
            f"width={wf.getsampwidth()}, "
            f"compression={wf.getcomptype()}"
        )
    # Create a recognizer with the sample rate from the file
    # Path to your downloaded Vosk model folder
    VOSK_MODEL_PATH = "Vosk_model"
    model = Model(VOSK_MODEL_PATH)
    if not model:
        raise ValueError(f"Model not found at {VOSK_MODEL_PATH}")
    recognizer = KaldiRecognizer(model, wf.getframerate())
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
    transcript = " ".join(filter(None, results))
    print("\n=== Transcript from user ===")
    print(transcript)
    return transcript