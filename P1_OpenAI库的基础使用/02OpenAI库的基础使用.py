from openai import OpenAI

# 1. 获取client对象，OpenAI类对象
client = OpenAI(
    base_url="http://192.168.1.80:11434/v1",
    api_key=""
)

# 2. 调用模型
response = client.chat.completions.create(
    model="qwen3:4b",
    messages=[
        # 设定模型的行为和准测
        {"role": "system", "content": "你是一个Python编程专家，并且不说废话简单回答"},
        # 设定模型的回答，由用户设定
        {"role": "assistant", "content": "好的，我是编程专家，并且话不多，你要问什么？"},
        # 用户提问
        {"role": "user", "content": "输出1-10的数字，使用python代码"}
    ]
)

# 3. 处理结果
print(response.choices[0].message.content)
