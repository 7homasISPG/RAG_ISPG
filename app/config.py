# --- START OF FILE config.py ---

import os
from dotenv import load_dotenv

load_dotenv()  # Load from .env file if present

class Settings:
    # OpenAI or other LLM provider
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")
    LLM_MODEL_NAME: str = os.getenv("LLM_MODEL_NAME", "gpt-3.5-turbo")
    
    # Embedding model
    EMBEDDING_MODEL_NAME: str = os.getenv("EMBEDDING_MODEL_NAME", "text-embedding-3-small")
    EMBEDDING_DIMENSION: int = int(os.getenv("EMBEDDING_DIMENSION", "1536")) # 1536 for small, 3072 for large

    # Vector DB config (Pinecone)
    PINECONE_API_KEY: str = os.getenv("PINECONE_API_KEY", "")
    PINECONE_ENV: str = os.getenv("PINECONE_ENV", "")
    PINECONE_INDEX_NAME: str = os.getenv("PINECONE_INDEX_NAME", "ispg-rag-index")
    
    # Multilingual support
    ENABLE_TRANSLATION: bool = os.getenv("ENABLE_TRANSLATION", "true").lower() == "true"
    
    # Logging config
    LOG_DB_PATH: str = os.getenv("LOG_DB_PATH", "logs/queries.db")
    
    # Supported languages
    SUPPORTED_LANGUAGES = ["en", "ar"]

settings = Settings()
