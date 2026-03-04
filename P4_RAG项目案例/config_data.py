# 文件的 MD5 值保存文件
md5_path = "./md5.text"

# Chroma
collection_name = "rag"
persist_directory = "./chroma_db"

# spliter
chunk_size = 500
chunk_overlap = 50
separators = ["\n\n", "\n", ".", "!", "?", "。", "！", "？", " ", ""]
max_split_char_number = 500  # 文本分割的阈值

# 检索返回匹配的文档数量
similarity_threshold = 1

# Ollama 配置（本地或远程）
use_local_model = True  # 是否使用 Ollama 模型（True=Ollama, False=阿里云 DashScope）
ollama_base_url = "http://192.168.1.80:11434"  # Ollama 服务地址，远程服务器改为对应 IP，如："http://192.168.1.100:11434"
local_embedding_model = "mxbai-embed-large:latest"  # Ollama 嵌入模型名称
local_chat_model = "qwen3:4b"  # Ollama 聊天模型名称

# 你的阿里云 DashScope API 密钥
dashscope_api_key = ""
embedding_model_name = "mxbai-embed-large:latest"
chat_model_name = "qwen3:4b"

# 会话配置
session_config = {
    "configurable": {
        "session_id": "user_001",
    }
}

# 会话历史存储
history_storage_path = "./chat_history"
