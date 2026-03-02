from openai import OpenAI

# 1. 获取client对象，OpenAI类对象
client = OpenAI(
    base_url="http://192.168.1.80:11434/v1",
    api_key=""
)

try:
    # 2. 调用模型
    response = client.chat.completions.create(
        model="qwen3:4b",
        messages=[
            {"role": "system", "content": "你是AI助理，回答很简洁"},
            {"role": "user", "content": "小明有2条宠物狗"},
            {"role": "assistant", "content": "好的"},
            {"role": "user", "content": "小红有3只宠物猫"},
            {"role": "assistant", "content": "好的"},
            {"role": "user", "content": "总共有几个宠物？"}
        ],
        stream=True
    )
    # 3. 处理结果
    for chunk in response:
        content = chunk.choices[0].delta.content
        if content:
            print(content, end=" ", flush=True)
except Exception as e:
    print(f"请求出错: {e}")
