# Architecture Diagram (Agents)

![RAG Chatbot Agent Architecture](https://i.imgur.com/4pXf4iv.png)

**Workflow:**
- **User:** Interacts via Streamlit UI (uploads docs, asks queries).
- **DocumentIngestionAgent:** Receives uploaded files, extracts, chunks, embeds, and stores in Chroma DB.
- **RAGChatAgent:** Receives user query, embeds it, retrieves relevant chunks, passes context to Llama 3.2+ for response.
- **Chroma Vector DB:** Stores document embeddings and metadata.
- **LLM (Llama 3.2+):** Generates context-grounded answers.
- **Agents (Langchain):** Orchestrate all steps, enabling modular, extensible, and scalable logic.

---