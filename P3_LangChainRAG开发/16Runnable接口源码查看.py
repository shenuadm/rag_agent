from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi
import os

# 设置环境变量（必须在导入和使用之前设置）
os.environ["DASHSCOPE_API_KEY"] = "sk-bca3c9259bce4a6ebf60f9f3f0372025"

prompt = PromptTemplate.from_template("你是一个AI助手")
model = Tongyi(model="qwen3-max")

chain = prompt | model | prompt | model
chain.invoke()
chain.stream()
print(type(chain))
