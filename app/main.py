from fastapi import FastAPI
from app.api.routes import router as api_router

app = FastAPI(
    title="ISPG RAG-Based Q&A Assistant",
    description="Multilingual chatbot using RAG to answer product and company-related queries",
    version="1.0.0"
)

app.include_router(api_router, prefix="/api")

@app.get("/")
async def root():
    return {"message": "ISPG Q&A Assistant is running!"}
