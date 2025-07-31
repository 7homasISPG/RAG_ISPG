# --- START OF FILE usage.py ---

from app.data.loader import load_multiple_urls
from app.data.chunker import chunk_documents
from app.data.embedder import embed_and_store_chunks

URLS = [
    "https://www.ispg.co/en",
    "https://www.ispg.co/en/solutions",
    "https://www.ispg.co/en/about"
]

def build_vector_index():
    print("Loading documents from URLs...")
    raw_docs = load_multiple_urls(URLS)
    
    print("Chunking documents...")
    chunks = chunk_documents(raw_docs)
    
    print(f"Generated {len(chunks)} chunks. Embedding and storing in vector store...")
    embed_and_store_chunks(chunks)
    
    print("Vector index build complete.")

if __name__ == "__main__":
    build_vector_index()
