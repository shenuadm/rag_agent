from langchain.agents import create_agent
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
import config_data as config


@tool(description="获取体重，返回值是整数，单位千克")
def get_weight() -> int:
    return 90


@tool(description="获取身高，返回值是整数，单位厘米")
def get_height() -> int:
    return 172


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
    tools=[get_weight, get_height],
    system_prompt="""你是严格遵循 ReAct 框架的智能体，必须按「思考→行动→观察→再思考」的流程解决问题，
    且**每轮仅能思考并调用 1 个工具**，禁止单次调用多个工具。
    并告知我你的思考过程，工具的调用原因，按思考、行动、观察三个结构告知我""",
)

for chunk in agent.stream(
        {"messages": [{"role": "user", "content": "计算我的 BMI"}]},
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
