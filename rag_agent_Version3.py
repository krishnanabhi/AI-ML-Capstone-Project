"""
Langchain Tool and Agent for Retrieval-Augmented Generation (RAG)
- Embeds user query
- Retrieves relevant contexts from Chroma
- Generates answer using Llama 3.2+
"""

from langchain.llms import LlamaCpp
from langchain.embeddings import NomicEmbedText
from chromadb import Client
from langchain.tools import Tool

def retrieve_docs(query, top_k=3):
    """
    Retrieve relevant document chunks for a query.
    """
    client = Client()
    collection = client.get_or_create_collection("knowledge_repo")
    embedder = NomicEmbedText()
    query_embedding = embedder.embed_query(query)
    results = collection.query(embeddings=[query_embedding], n_results=top_k)
    return "\n".join([doc for doc in results["documents"][0]])

def generate_answer(context, query):
    """
    Generate answer from LLM given context and query.
    """
    llm = LlamaCpp(model_path="llama-3.2.bin")
    prompt = f"Context:\n{context}\n\nQuestion: {query}\nAnswer:"
    try:
        answer = llm(prompt)
    except Exception:
        answer = "Sorry, I couldn't process your question due to an internal error."
    return answer

def rag_agent(query):
    """
    RAG Agent main entry point.
    - Retrieves relevant context
    - Calls LLM for answer
    """
    context = retrieve_docs(query)
    if not context or context.strip() == "":
        return "Sorry, I couldn't find an answer to your question in the uploaded documents."
    return generate_answer(context, query)

# Langchain Tool for RAG
rag_tool = Tool(
    name="RAGChatAgent",
    func=rag_agent,
    description="Retrieves relevant context and generates answers using Llama 3.2+."
)