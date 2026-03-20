from langchain_ollama import OllamaEmbeddings

model = OllamaEmbeddings(
    base_url="http://192.168.1.80:11434",
    model="mxbai-embed-large:latest"
)

# 不用invoke stream
# embed_query、embed_documents
print(model.embed_query("我喜欢你"))
print(model.embed_documents(["我喜欢你", "我稀饭你", "晚上吃啥"]))
