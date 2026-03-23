from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS


def ingest_pdf(file_path: str, persist_path: str = "vectorstore"):
    loader = PyPDFLoader(file_path)
    documents = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
    docs = splitter.split_documents(documents)

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)

    vectorstore.save_local(persist_path)
    print("Ingestion complete!")


if __name__ == "__main__":
    ingest_pdf("data/sample.pdf")
