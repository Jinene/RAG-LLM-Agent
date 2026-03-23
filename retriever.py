from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS


def load_retriever(persist_path="vectorstore"):
    embeddings = OpenAIEmbeddings()
    db = FAISS.load_local(persist_path, embeddings)
    return db.as_retriever()
