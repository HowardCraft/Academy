#!/usr/bin/env python3
"""
run_tinyllama.py

A formal, argument-driven script to load and interact with the TinyLLaMA model via the llama-cpp-python bindings.

Usage:
    python run_tinyllama.py \  # or execute directly if chmod +x
        --model-path PATH_TO_MODEL \  # GGUF model file
        --prompt "Your prompt here" \  # question or conversation starter
        [--max-tokens N] \           # maximum number of tokens to generate
        [--temperature T] \          # randomness control
        [--repeat-penalty R] \       # penalty for repeated tokens
        [--context-length C]          # context window size

Example:
    python run_tinyllama.py \
        --model-path tinyllama-models/tinyllama-1.1b-chat-v1.0.Q8_0.gguf \
        --prompt "Hello, students! Share a fun fact about penguins." \
        --max-tokens 50 \
        --temperature 0.7 \
        --repeat-penalty 1.1 \
        --context-length 2048
"""
import argparse
import sys
from llama_cpp import Llama

def parse_args():
    parser = argparse.ArgumentParser(
        description="Interact with TinyLLaMA through llama-cpp-python bindings."
    )
    parser.add_argument(
        "--model-path", type=str, required=True,
        help="Path to the TinyLLaMA GGUF model file"
    )
    parser.add_argument(
        "--prompt", type=str, required=True,
        help="Text prompt to send to the model"
    )
    parser.add_argument(
        "--max-tokens", type=int, default=50,
        help="Maximum number of tokens to generate (default: 50)"
    )
    parser.add_argument(
        "--temperature", type=float, default=0.7,
        help="Sampling temperature; higher values produce more random output (default: 0.7)"
    )
    parser.add_argument(
        "--repeat-penalty", type=float, default=1.1,
        help="Penalty for repeated tokens; values >1 discourage repetition (default: 1.1)"
    )
    parser.add_argument(
        "--context-length", type=int, default=2048,
        help="Context window size in tokens (default: 2048)"
    )
    return parser.parse_args()

def main():
    args = parse_args()

    # Load the TinyLLaMA model
    print(f"Loading TinyLLaMA model from: {args.model_path}")
    try:
        llm = Llama(
            model_path=args.model_path,
            n_ctx=args.context_length,
            temperature=args.temperature,
            repeat_penalty=args.repeat_penalty
        )
    except Exception as e:
        print(f"Error loading model: {e}", file=sys.stderr)
        sys.exit(1)

    # Generate a response
    print(f"\nPrompt: {args.prompt}\nGenerating up to {args.max_tokens} tokens...\n")
    try:
        response = llm(
            args.prompt,
            max_tokens=args.max_tokens
        )
    except Exception as e:
        print(f"Error during inference: {e}", file=sys.stderr)
        sys.exit(1)

    # Output result
    text = response.choices[0].text.strip()
    print(f"🤖 TinyLLaMA says:\n{text}\n")

if __name__ == "__main__":
    main()
