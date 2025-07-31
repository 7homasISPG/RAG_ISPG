# --- START OF FILE app/rag/retriever.py (Final Corrected Version) ---

from app.config import settings
from pinecone import Pinecone, PodSpec # Import PodSpec for index creation
from langchain_community.vectorstores import Pinecone as LangchainPinecone
from langchain_openai import OpenAIEmbeddings

# --- 1. Initialize Pinecone Client ---
# This remains correct.
pc = Pinecone(api_key=settings.PINECONE_API_KEY)
index_name = settings.PINECONE_INDEX_NAME

# --- 2. Initialize Embedding Model ---
# This remains correct.
embedding_model = OpenAIEmbeddings(
    model=settings.EMBEDDING_MODEL_NAME,
    openai_api_key=settings.OPENAI_API_KEY
)

# --- 3. Ensure the index exists ---
# This logic is also correct.
if index_name not in pc.list_indexes().names():
    print(f"Index '{index_name}' not found. Creating a new one...")
    pc.create_index(
        name=index_name,
        dimension=settings.EMBEDDING_DIMENSION,
        metric="cosine",
        spec=PodSpec(
            environment=settings.PINECONE_ENV,
            pod_type="p1.x1" # Or another pod type like 's1.x1'
        )
    )

# --- 4. Create the LangChain vector store ---
#
# THIS IS THE KEY CHANGE.
# LangChain now handles getting the index object itself.
# We pass the index_name and the initialized embedding model.
# The `from_existing_index` method will use the default Pinecone client
# that is automatically configured when you instantiate `Pinecone()`.
#
vector_store = LangchainPinecone.from_existing_index(
    index_name=index_name,
    embedding=embedding_model
)

# --- 5. Define the retriever and getter functions ---
# These functions now work with the correctly initialized vector_store.

def get_retriever(search_k: int = 4):
    """Returns a retriever instance from the global vector store."""
    return vector_store.as_retriever(search_kwargs={'k': search_k})

def get_vector_store():
    """Returns the global vector store instance for adding documents."""
    return vector_store