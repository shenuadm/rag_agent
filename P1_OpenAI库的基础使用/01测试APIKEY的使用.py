from openai import OpenAI

# 创建 OpenAI 客户端
client = OpenAI(
    base_url="http://192.168.1.80:11434/v1",
    api_key=""
)

# 创建聊天
completion = client.chat.completions.create(
    model="qwen3:4b",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你是谁，能做什么？"},
    ],
    stream=True
)

# 打印结果
for chunk in completion:
    print(chunk.choices[0].delta.content, end="", flush=True)
