from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA
from retriever import load_retriever


def build_agent():
    retriever = load_retriever()

    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain
