# --- START OF FILE app/rag/pipeline.py (Corrected) ---

from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI  # <-- CORRECTED IMPORT
from app.rag.retriever import get_retriever
from app.rag.prompt_template import get_prompt_template
from app.config import settings
from langchain.prompts import PromptTemplate

def get_rag_answer(query: str, lang: str = "en"):
    # 1. Prepare retriever and LLM
    retriever = get_retriever()
    llm = ChatOpenAI( # This object creation remains the same
        temperature=0.2,
        model_name=settings.LLM_MODEL_NAME,
        openai_api_key=settings.OPENAI_API_KEY
    )

    # ... rest of the file is correct and remains the same ...
    # 2. Setup prompt
    template_str = get_prompt_template(lang)
    prompt = PromptTemplate(input_variables=["context", "question"], template=template_str)

    # 3. Setup RAG chain
    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )

    # 4. Run query
    result = qa_chain({"query": query})
    answer = result["result"]
    
    # 5. Extract source URLs if present
    sources = []
    if result.get("source_documents"):
        for doc in result["source_documents"]:
            if "source" in doc.metadata:
                sources.append(doc.metadata["source"])

    return answer, sources