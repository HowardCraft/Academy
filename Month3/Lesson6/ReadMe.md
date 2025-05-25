# TinyLLaMA Classroom Toolkit

This repository provides two scripts to help beginner students install and interact with the TinyLLaMA model on a Raspberry Pi:

- **InstallRequirments.sh** – Automated Bash installer that:
  1. Installs system dependencies
  2. Downloads the TinyLLaMA GGUF model
  3. Installs the Python bindings via `llama-cpp-python`
  4. Verifies the installation with a sample inference

- **run test_llama.py** – A formal, argparse‑driven Python script to load the TinyLLaMA model and generate text from a user-specified prompt.


## Installation & Setup



## Usage

###  Using the Python script
Run `test_llama.py` with your own prompt and parameters:

```bash
python3 test_llama.py \
  --model-path "$HOME/tinyllama-models/tinyllama-1.1b-chat-v1.0.Q8_0.gguf" \
  --prompt "What is a fascinating fact about space?" \
  --max-tokens 60 \
  --temperature 0.8 \
  --repeat-penalty 1.2 \
  --context-length 2048
```

#### Script Options

| Flag               | Description                                              | Default    |
|--------------------|----------------------------------------------------------|------------|
| `--model-path`     | Path to the GGUF model file                              | *required* |
| `--prompt`         | Text prompt to send to TinyLLaMA                         | *required* |
| `--max-tokens`     | Maximum tokens to generate                               | `50`       |
| `--temperature`    | Sampling temperature (higher = more random)               | `0.7`      |
| `--repeat-penalty` | Penalty for repeated tokens (>1 discourages repetition)  | `1.1`      |
| `--context-length` | Context window size in tokens                            | `2048`     |

## Troubleshooting

- **Out of memory errors**: Ensure you downloaded the 4‑bit Q8_0 model and have at least 8 GB RAM.
- **C++ build failures**: Install `build-essential` and `cmake` via `sudo apt install -y build-essential cmake`.
- **Slow inference**: Quantization and smaller context lengths speed up performance.

---

Happy experimenting! 🎉

*Questions? Feel free to open an issue or ask your instructor.*
