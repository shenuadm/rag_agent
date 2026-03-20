from langchain_core.prompts import PromptTemplate
from langchain_community.llms.tongyi import Tongyi
import os

# 设置环境变量（必须在导入和使用之前设置）
os.environ["DASHSCOPE_API_KEY"] = "sk-bca3c9259bce4a6ebf60f9f3f0372025"

# zero-shot
prompt_template = PromptTemplate.from_template(
    "我的邻居姓{lastname}, 刚生了{gender}, 你帮我起个名字，简单回答。"
)
model = Tongyi(model="qwen-max")

# 调用.format方法注入信息即可
# prompt_text = prompt_template.format(lastname="张", gender="女儿")
#
# model = Tongyi(model="qwen-max")
# res = model.invoke(input=prompt_text)
# print(res)

chain = prompt_template | model

res = chain.invoke(input={"lastname": "张", "gender": "女儿"})
print(res)
