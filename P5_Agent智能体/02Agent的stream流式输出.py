from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
import config_data as config


@tool(description="获取股价，传入股票名称，返回字符串信息")
def get_price(name: str) -> str:
    return f"股票{name}的价格是 20 元"


@tool(description="获取股票信息，传入股票名称，返回字符串信息")
def get_info(name: str) -> str:
    return f"股票{name}，是一家 A 股上市公司，专注于 IT 职业教育。"


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
    model=chat_model,
    tools=[get_price, get_info],
    system_prompt="你是一个智能助手，可以回答股票相关问题，记住请告知我思考过程，让我知道你为什么调用某个工具"
)

for chunk in agent.stream(
        {"messages": [{"role": "user", "content": "传智教育股价多少，并介绍一下"}]},
        stream_mode="values"
):
    latest_message = chunk['messages'][-1]

    if latest_message.content:
        print(type(latest_message).__name__, latest_message.content)

    try:
        if latest_message.tool_calls:
            print(f"工具调用：{[tc['name'] for tc in latest_message.tool_calls]}")
    except AttributeError as e:
        pass
