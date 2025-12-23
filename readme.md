```markdown
# ClauseAI 📑

**A Smart Legal Document Analysis System powered by LLMs and RAG**

Imagine having a legal assistant who reads every clause for you before you sign. That's the experience ClauseAI aims to provide.

ClauseAI allows you to upload and intelligently query legal documents (contracts, NDAs, agreements, etc.) using natural language. It helps uncover risks, obligations, summaries, and even comparisons across multiple documents — making contract review faster, more reliable, and accessible.

## ✨ Features

- **Multi-Document Upload**: Upload one or multiple legal PDFs (contracts, NDAs, agreements).
- **Ultra-Fast Document Loading**: Powered by PyMuPDF for quick ingestion, even with large files.
- **Efficient Indexing & Retrieval**: Optimized semantic search using FAISS for fast and accurate results.
- **LLM-Driven Query Routing**: Intelligently decides which documents are relevant to your question.
- **Multi-Document Orchestration**: Handles complex queries across documents, ensuring grounded, concise, and context-aware responses.
- **Natural Language Queries**: Ask anything — summarize clauses, identify risks/obligations, compare terms, and more.

## 🤔 Why ClauseAI?

Legal documents are dense, time-consuming, and prone to misinterpretation. ClauseAI leverages Retrieval-Augmented Generation (RAG) to make understanding contracts easier and more accurate, saving time for professionals and individuals alike.

This project is an important step in exploring LLM-driven systems with LlamaIndex and Generative AI.

## 🛠️ Tech Stack

- **LlamaIndex** → Document indexing, retrieval, and query engines
- **Groq LLMs** → Low-latency reasoning and generation
- **PyMuPDF** → High-performance PDF loading
- **FAISS** → Fast vector-based semantic search
- **Streamlit** → Interactive web UI

## 🚀 Live Demo

Try ClauseAI live here: [https://clause-ai.streamlit.app/](https://clause-ai.streamlit.app/)

## 📦 Installation & Local Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/Prince-darji-2306/ClauseAI.git
   cd ClauseAI
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the app locally:
   ```bash
   streamlit run app.py
   ```

> Note: You'll need an API key for Groq. Set it as an environment variable (e.g., `export GROQ_API_KEY=your_key`).

## 💡 Usage Examples

- Upload a contract and ask: "What are my payment obligations?"
- Upload multiple NDAs and ask: "Compare the non-compete clauses across these documents."
- "Summarize the termination conditions."
- "Highlight any potential risks in this agreement."

## 🚧 Status & Contributions

ClauseAI is still evolving! Feedback, ideas, bug reports, and contributions are very welcome.

- Open an issue for suggestions or bugs.
- Submit a pull request for improvements.

#GenerativeAI #LlamaIndex #DocumentAI #LegalTech #RAG #AIProjects #Groq #Streamlit #LearningByBuilding

---
Made with ❤️ by [Prince Darji](https://github.com/Prince-darji-2306)
```