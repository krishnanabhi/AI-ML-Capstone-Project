"""
Unit Tests for RAG Chatbot Agents
- Test document extraction, chunking, agent calls, error cases
"""

import pytest
from ingest_agent import extract_text, chunk_text, ingest_documents
from rag_agent import retrieve_docs, generate_answer, rag_agent

def test_extract_text_txt(tmp_path):
    # Create a sample txt file
    txt_file = tmp_path / "sample.txt"
    txt_file.write_text("Hello World! This is a test document.")
    with open(txt_file, "rb") as file:
        file.name = "sample.txt"
        text = extract_text(file)
        assert "Hello World!" in text

def test_chunk_text():
    text = "A" * 1200
    chunks = chunk_text(text, chunk_size=500)
    assert len(chunks) == 3
    assert all(len(chunk) <= 500 for chunk in chunks)

def test_ingest_documents_invalid_file():
    class DummyFile:
        name = "image.png"
        def read(self): return b""
    assert ingest_documents([DummyFile()]) == False

def test_rag_agent_no_context(monkeypatch):
    # Monkeypatch retrieval to return empty context
    monkeypatch.setattr("rag_agent.retrieve_docs", lambda q: "")
    response = rag_agent("Test query")
    assert "couldn't find an answer" in response

# Add more tests as needed for integration and error handling