# RAG Chatbot with Langchain Agents

## Description

This repository contains a conversational chatbot that answers user queries by retrieving relevant chunks from custom knowledge documents (PDF/TXT) and generating answers via an LLM (Llama 3.2+). The solution uses **Langchain Agents** for modular orchestration of document ingestion, retrieval, and chat response.

## Technologies

- Python 3.13.x
- Langchain (agents, tools)
- Llama 3.2 or higher (Open Source)
- nomic-embed-text (Embeddings)
- Chroma (Vector DB)
- Streamlit (UI)
- PyPDF2 (PDF parsing)

## Architecture

1. **User uploads document via Streamlit UI**
2. **Document Ingestion Agent** parses, chunks, embeds, and stores content in Chroma DB.
3. **Chat Agent** receives user query, embeds it, retrieves relevant context from Chroma, passes context to Llama for answer generation, and handles error cases.
4. **Agents use Langchain Tools** for modular, extensible action.

## How Agents Work in this Solution

- **DocumentIngestionAgent**: Handles file parsing, chunking, embedding, and storage.
- **ChatAgent (RAGAgent)**: Handles query embedding, vector search, context assembly, and LLM answer generation.

## Running the Solution

1. `pip install -r requirements.txt`
2. Download `llama-3.2.bin` and place in root directory.
3. `streamlit run app.py`
4. Upload documents, ask questions.
