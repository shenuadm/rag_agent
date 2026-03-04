from langchain_chroma import Chroma
from langchain_community.embeddings import DashScopeEmbeddings

import config_data as config
from langchain_ollama import OllamaEmbeddings


class VectorStoreService(object):
    def __init__(self, embedding=None):
        """
        :param embedding: 嵌入模型的传入，如果不传则使用配置文件的默认设置
        """
        # 如果没有传入 embedding，则根据配置自动选择
        if embedding is None:
            if config.use_local_model:
                self.embedding = OllamaEmbeddings(
                    model=config.local_embedding_model,
                    base_url=config.ollama_base_url
                )
            else:
                self.embedding = DashScopeEmbeddings(
                    model=config.embedding_model_name,
                    dashscope_api_key=config.dashscope_api_key
                )
        else:
            self.embedding = embedding

        self.vector_store = Chroma(
            collection_name=config.collection_name,
            embedding_function=self.embedding,
            persist_directory=config.persist_directory,
        )

    def get_retriever(self):
        """返回向量检索器，方便加入 chain"""
        return self.vector_store.as_retriever(search_kwargs={"k": config.similarity_threshold})


if __name__ == '__main__':
    # 使用默认的嵌入模型（根据配置文件自动选择本地或云端）
    retriever = VectorStoreService().get_retriever()

    res = retriever.invoke("我的体重 180 斤，尺码推荐")
    print(res)
