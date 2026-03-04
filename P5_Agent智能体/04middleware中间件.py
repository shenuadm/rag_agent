from langchain.agents import create_agent, AgentState
from langchain.agents.middleware import before_agent, after_agent, before_model, after_model, wrap_model_call, \
    wrap_tool_call
from langchain_community.chat_models.tongyi import ChatTongyi
from langchain_ollama import ChatOllama
from langchain_core.tools import tool
from langgraph.runtime import Runtime
import config_data as config


@tool(description="查询天气，传入城市名称字符串，返回字符串天气信息")
def get_weather(city: str) -> str:
    return f"{city}天气：晴天"


"""
1. agent 执行前
2. agent 执行后
3. model 执行前
4. model 执行后
5. 工具执行中
6. 模型执行中
"""


@before_agent
def log_before_agent(state: AgentState, runtime: Runtime) -> None:
    # agent 执行前会调用这个函数并传入 state 和 runtime 两个对象
    print(f"[before agent]agent 启动，并附带{len(state['messages'])}消息")


@after_agent
def log_after_agent(state: AgentState, runtime: Runtime) -> None:
    print(f"[after agent]agent 结束，并附带{len(state['messages'])}消息")


@before_model
def log_before_model(state: AgentState, runtime: Runtime) -> None:
    print(f"[before_model]模型即将调用，并附带{len(state['messages'])}消息")


@after_model
def log_after_model(state: AgentState, runtime: Runtime) -> None:
    print(f"[after_model]模型调用结束，并附带{len(state['messages'])}消息")


@wrap_model_call
def model_call_hook(request, handler):
    print("模型调用啦")
    return handler(request)


@wrap_tool_call
def monitor_tool(request, handler):
    print(f"工具执行：{request.tool_call['name']}")
    print(f"工具执行传入参数：{request.tool_call['args']}")

    return handler(request)


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
    tools=[get_weather],
    middleware=[log_before_agent, log_after_agent, log_before_model, log_after_model, model_call_hook, monitor_tool]
)

res = agent.invoke({"messages": [{"role": "user", "content": "深圳今天的天气如何呀，如何穿衣"}]})
print("**********\n", res)
