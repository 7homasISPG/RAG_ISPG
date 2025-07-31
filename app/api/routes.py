# --- START OF FILE routes.py ---

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.rag.pipeline import get_rag_answer
from app.utils.language_detect import detect_language
from app.db.logger import log_query
from app.config import settings

router = APIRouter()

class QueryRequest(BaseModel):
    query: str
    lang: Optional[str] = None  # Make lang optional

class QueryResponse(BaseModel):
    answer: str
    source_documents: list[str] = []

@router.post("/ask", response_model=QueryResponse)
async def ask_question(payload: QueryRequest):
    if not payload.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty.")
    

    lang = payload.lang
    if lang not in settings.SUPPORTED_LANGUAGES:
        lang = detect_language(payload.query)
        if lang not in settings.SUPPORTED_LANGUAGES:
            lang = "en"

    try:
        answer, sources = get_rag_answer(payload.query, lang)
        log_query(payload.query, answer, lang)
        # Ensure unique sources
        unique_sources = sorted(list(set(sources)))
        return QueryResponse(answer=answer, source_documents=unique_sources)
    except Exception as e:
        # It's good practice to log the actual error for debugging
        print(f"An error occurred: {e}")
        raise HTTPException(status_code=500, detail="An internal error occurred while processing your request.")