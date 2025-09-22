"""
Streamlit UI for RAG Chatbot
- Upload documents (PDF/TXT)
- Chat interface using Langchain Agents
"""

import streamlit as st
from ingest_agent import ingest_tool
from rag_agent import rag_tool

st.set_page_config(page_title="RAG Chatbot (Agents)", layout="wide")
st.title("Conversational RAG Chatbot (Langchain Agents)")

# ---------- Document Upload Section ----------
st.header("Upload Documents (PDF or TXT)")
uploaded_files = st.file_uploader("Choose PDF/TXT files", accept_multiple_files=True)

if st.button("Ingest Documents") and uploaded_files:
    # Call Langchain Tool (Agent) for ingestion
    success = ingest_tool.func(uploaded_files)
    if success:
        st.success("Documents ingested successfully!")
    else:
        st.error("Failed to ingest documents. Please check file formats.")

# ---------- Chat Interface Section ----------
st.header("Chatbot Interface")
query = st.text_input("Ask a question about your documents:")

if st.button("Get Answer") and query:
    # Call RAG Agent Tool for answer
    response = rag_tool.func(query)
    st.markdown(f"**Bot:** {response}")

# ---------- UI Notes ----------
st.markdown("""
*Note: Only PDF/TXT files are supported for uploads.  
Agent-based architecture ensures modularity and extensibility.*
""")