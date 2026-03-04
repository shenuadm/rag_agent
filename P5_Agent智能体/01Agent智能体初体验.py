from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
import config_data as config


@tool(description="查询天气")
def get_weather() -> str:
    return "晴天"


# 根据配置选择使用本地模型还是云端模型
if config.use_local_model:
    # 使用本地/远程 Ollama 模型
    chat_model = ChatOllama(
        model=config.local_chat_model,
        base_url=config.ollama_base_url
    )
else:
    # 使用阿里云 DashScope 云端模型
    chat_model = ChatTongyi(
        model=config.chat_model_name,
        dashscope_api_key=config.dashscope_api_key
    )

agent = create_agent(
    model=chat_model,  # 智能体的大脑 LLM
    tools=[get_weather],  # 向智能体提供工具列表
    system_prompt="你是一个聊天助手，可以回答用户问题。",
)

res = agent.invoke(
    {
        "messages": [
            {"role": "user", "content": "明天深圳的天气如何？"},
        ]
    }
)

for msg in res["messages"]:
    print(type(msg).__name__, msg.content)
