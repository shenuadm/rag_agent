# langchain_community
from langchain_community.llms.tongyi import Tongyi
import os

# 设置环境变量（必须在导入和使用之前设置）
os.environ["DASHSCOPE_API_KEY"] = "sk-bca3c9259bce4a6ebf60f9f3f0372025"

# 不用qwen3-max，因为qwen3-max是聊天模型，qwen-max是大语言模型
model = Tongyi(
    model="qwen-max"
)

# 调用invoke向模型提问
res = model.invoke(input="你是谁呀能做什么？")

print(res)
