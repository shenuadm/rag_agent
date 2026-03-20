# langchain_ollama
from langchain_ollama import OllamaLLM

model = OllamaLLM(
    base_url="http://192.168.1.80:11434",
    model="qwen3:4b"
)

res = model.invoke(input="你是谁呀能做什么？")

print(res)
