"""
Langchain Tool and Agent for Document Ingestion
- Parses PDF/TXT files
- Chunks text
- Embeds with nomic-embed-text
- Stores in Chroma DB
"""

from PyPDF2 import PdfReader
from langchain.embeddings import NomicEmbedText
from chromadb import Client
from langchain.tools import Tool

def extract_text(file):
    """
    Extract text from PDF or TXT file object.
    Returns text or None if unsupported.
    """
    if file.name.endswith(".pdf"):
        reader = PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() or ""
        return text
    elif file.name.endswith(".txt"):
        return file.read().decode("utf-8")
    else:
        return None

def chunk_text(text, chunk_size=500):
    """
    Split large text into chunks for embedding.
    """
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

def ingest_documents(files):
    """
    Main ingestion function.
    - Extracts and chunks text
    - Embeds chunks
    - Stores in Chroma DB
    Returns True if successful.
    """
    client = Client()
    # Knowledge base collection
    collection = client.get_or_create_collection("knowledge_repo")
    embedder = NomicEmbedText()
    ingested = False
    for file in files:
        text = extract_text(file)
        if not text:
            continue  # skip unsupported files
        chunks = chunk_text(text)
        embeddings = embedder.embed_documents(chunks)
        for chunk, embedding in zip(chunks, embeddings):
            collection.add(embeddings=[embedding], documents=[chunk])
        ingested = True
    return ingested

# Langchain Tool for ingestion
ingest_tool = Tool(
    name="DocumentIngestion",
    func=ingest_documents,
    description="Ingests PDF/TXT files into the vector DB."
)