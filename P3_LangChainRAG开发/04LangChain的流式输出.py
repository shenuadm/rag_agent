from langchain_community.llms.tongyi import Tongyi
import os

# 设置环境变量（必须在导入和使用之前设置）
os.environ["DASHSCOPE_API_KEY"] = "sk-bca3c9259bce4a6ebf60f9f3f0372025"

model = Tongyi(model="qwen-max")

# 通过stream方法获得流式输出
res = model.stream(input="你是谁呀能做什么？")

for chunk in res:
    print(chunk, end="", flush=True)

# from langchain_ollama import OllamaLLM
#
# model = OllamaLLM(
#     base_url="http://192.168.1.80:11434",
#     model="qwen3:4b"
# )
#
# res = model.stream(input="你是谁呀能做什么？")
#
# for chunk in res:
#     print(chunk, end="", flush=True)
