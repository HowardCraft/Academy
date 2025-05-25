# Speech Recognition and Text-to-Speech

## Introduction

This hands-on guide covers how to:

1. Test and configure your microphone.  
2. Capture audio input and convert speech to text.  
3. Generate spoken responses (Text-to-Speech) through your speakers.  

Whether you’re building voice-controlled applications, assistants, or accessibility tools, these exercises will walk you through the core concepts and code for working with audio in Python.

---

## Prerequisites

Before you begin, ensure that:

- You have **Python 3.7+** installed.  
- Your system has a working **microphone** and **speaker**.  
- You have a recent version of **pip** for installing packages.  

##  How to Install Dependencies

All required Python packages and system tools are specified in the `installRequirement.sh` script. To install:

```bash
# Make the installer executable (once)
chmod +x installRequirement.sh

# Run the installer
./installRequirement.sh
```

## Hands-On Tasks

First step is to activte virtualenv:
```bash
source vf_env/bin/activate
```

### 1. Microphone Test (`H1-micTest.py`)

Verify that your microphone is properly detected and can record audio.

**What it does:**

- Lists available audio input devices  
- Records a short audio clip  
- Saves the result as `mic_test.wav`  

**Run:**

```bash
python H1-micTest.py --duration 5 --filename test.wav
```



### 2. Speech Recognition from Mic (`H2-speechRecog.py`)

Capture live audio from your microphone and convert it to text.

**What it does:**

- Records audio for a specified duration  
- Prints the recognized text to the console  

**Run:**

```bash
python H2-transcribe2text.py 
```

Parameters:

--duration (float): Seconds to listen (default: 5.0)

--provider (str): Which STT engine to use (e.g., VOSK)



### 3. Text-to-Speech Response (`H3-talkBack.py`)

Convert text (either typed or transcribed) into spoken audio through your speakers.

**What it does:**

- Takes input text (from command line or previous transcription)  
- Plays the audio via your default speaker  

**Run:**

```bash
python H3-talkBack.py
```