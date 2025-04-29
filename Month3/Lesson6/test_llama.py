from llama_cpp import Llama

# Initialize the model (adjust path if you moved the file)
model_path = "tinyllama-models/tinyllama-1.1b-chat-v1.0.Q8_0.gguf"
llm = Llama(model_path=model_path)

# Run a simple prompt
response = llm("Hello, students! Tell me one fun fact about penguins.", max_tokens=50)
print("\n🤖 TinyLLaMA says:\n" + response.choices[0].text.strip())