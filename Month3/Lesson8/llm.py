import sys
from llama_cpp import Llama

def Run_llm(my_prompt):
    # Load the TinyLLaMA model
    model_path = "llama-2-7b-chat.gguf"
    print(f"Loading TinyLLaMA model from: {model_path}")
    try:
        llm = Llama(
            model_path=model_path,
            n_ctx=2048,
            temperature=0.5,
            repeat_penalty=1.1
        )
    except Exception as e:
        print(f"Error loading model: {e}", file=sys.stderr)
        sys.exit(1)

    prompt = (
"[INST] <<SYS>>"
"You are a helpful assistant that answers conversationally but precisely."
"<</SYS>>"


"Q: What’s the tallest mountain in the world?"
"A: Mount Everest is the tallest mountain on Earth, standing at 8,848 meters above sea level. It sits on the border of Nepal and China, and has been a major mountaineering challenge since the early 20th century. [/INST]"
"[INST]"+
my_prompt+
"A:"
)

    try:
        response = llm(
            prompt,
            max_tokens=2048
        )
    except Exception as e:
        print(f"Error during inference: {e}", file=sys.stderr)
        sys.exit(1)


    # Output result

    text = response["choices"][0]["text"].strip()
    print(f"🤖 TinyLLaMA says:\n{text}\n")
    return text
