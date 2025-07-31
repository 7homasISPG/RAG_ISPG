from langchain.text_splitter import RecursiveCharacterTextSplitter

def chunk_text(text: str, chunk_size: int = 500, chunk_overlap: int = 50) -> list[str]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap
    )
    return splitter.split_text(text)

def chunk_documents(docs: list[dict]) -> list[dict]:
    """Split each document into chunks with metadata."""
    chunks = []
    for doc in docs:
        text_chunks = chunk_text(doc["content"])
        for i, chunk in enumerate(text_chunks):
            chunks.append({
                "text": chunk,
                "metadata": {
                    "source": doc["url"],
                    "chunk_id": i
                }
            })
    return chunks
