from fastapi import FastAPI
from pydantic import BaseModel
from agent import build_agent

app = FastAPI()
agent = build_agent()

class Query(BaseModel):
    question: str

@app.post("/ask")
def ask(query: Query):
    result = agent({"query": query.question})
    return {"answer": result["result"]}
