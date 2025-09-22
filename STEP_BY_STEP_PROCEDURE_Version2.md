# Step-by-Step Guide: Running the RAG Chatbot with Agents (Langchain, Streamlit, Llama, Chroma)

---

## 1. **Install Python**

- Download and install **Python 3.13.x** from [python.org](https://www.python.org/downloads/).
- Ensure `python` and `pip` are available in your terminal.

---

## 2. **Set Up Your Project Directory**

- Create a new folder for your project, e.g. `rag-chatbot-agent`.
- Place all the provided files (`app.py`, `ingest_agent.py`, `rag_agent.py`, `requirements.txt`, `README.md`, etc.) in this folder.

---

## 3. **Download Llama Model**

- Download the **Llama 3.2+ model weights** (`llama-3.2.bin`) from HuggingFace or the official source.
- Place `llama-3.2.bin` in your project root folder.

---

## 4. **Create a Virtual Environment (Recommended)**

```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate
```

---

## 5. **Install Dependencies**

```bash
pip install -r requirements.txt
```

---

## 6. **Run the Streamlit App**

```bash
streamlit run app.py
```
- Your default browser should open to the Streamlit UI.
- If not, visit [http://localhost:8501](http://localhost:8501) manually.

---

## 7. **Upload Documents**

- In the UI, use the **Upload Documents** section to select and upload one or more PDF/TXT files.
- Click **"Ingest Documents"** to process and store them in the vector DB.

---

## 8. **Chat with the Bot**

- Enter your question in the **Chatbot Interface** text box.
- Click **"Get Answer"**.
- The agent will retrieve relevant document context and generate an answer using the Llama model.

---

## 9. **Troubleshooting**

- If you see errors about the model, confirm that `llama-3.2.bin` is present and the path in code matches.
- Only PDF and TXT files are supported.
- For dependency issues, ensure your Python version is correct and all packages are installed.

---

## 10. **How Agents Work (Quick Recap)**

- **Ingestion Agent:** Parses, chunks, embeds, and stores uploaded docs.
- **Chat Agent:** Embeds user query, retrieves relevant chunks, uses Llama to generate answer.

---

## 11. **Customizing or Extending**

- To change chunk size, embedding model, or LLM, adjust parameters in `ingest_agent.py` and `rag_agent.py`.
- You can add more agent tools for tasks like summarization, document extraction, or multi-hop reasoning.

---

## 12. **Testing**

- Run `pytest test_app.py` to execute unit tests (if you have pytest installed).

---

**You now have a fully working agent-based RAG chatbot!**