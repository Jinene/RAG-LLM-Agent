# RAG-LLM-Agent
This is a simple Retrieval-Augmented Generation (RAG) system using LangChain, FAISS, and OpenAI.

## Features
- PDF ingestion
- Vector search with FAISS
- LLM-powered Q&A
- CLI + API support

## Setup

```bash
git clone <your-repo>
cd rag-llm-agent
pip install -r requirements.txt
```

## Add your API key

Create a `.env` file:

```
OPENAI_API_KEY=your_key_here
```

## Ingest documents

```bash
python ingest.py
```

## Run CLI

```bash
python main.py
```

## Run API

```bash
uvicorn api:app --reload
```

## Example API Call

```bash
curl -X POST "http://127.0.0.1:8000/ask" \
-H "Content-Type: application/json" \
-d '{"question": "What is this document about?"}'
```

## Future Improvements
- Add memory
- Add multi-doc support
- Add UI (Streamlit)
- Add evaluation metrics
