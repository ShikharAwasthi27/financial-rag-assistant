from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Financial RAG API"}


@app.post("/ask")
def ask(query: str):

    result = rag.generate_answer(query)

    return result
