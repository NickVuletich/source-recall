# ContextPilot — Local RAG Workflow Assistant

ContextPilot is a local retrieval-augmented generation system for querying messy notes, logs, and documents. It is designed to work across multiple domains, including fitness logs, business notes, project documentation, client records, and internal workflow data.

The project focuses on building the core RAG pipeline without hiding everything behind a large framework: document ingestion, chunking, embeddings, vector storage, retrieval, prompt construction, local LLM generation, and basic evaluation.

## Why I Built This

I built ContextPilot to understand how practical RAG systems work beyond demos. Instead of only calling an LLM directly, this project retrieves relevant source context first, then uses that context to generate grounded answers.

The first sample data includes fitness and business-style notes, but the pipeline is domain-agnostic and can be reused for other document types.

## Features

- Load `.md` and `.txt` documents from `data/raw/`
- Split documents into overlapping text chunks
- Create local embeddings using Sentence Transformers
- Store chunks in ChromaDB
- Retrieve relevant chunks for a natural language query
- Generate grounded answers with a local Ollama model
- Print source chunks used in the answer

## Tech Stack

- Python
- ChromaDB
- Sentence Transformers
- Ollama
- Typer
- Rich

## Project Structure

```txt
contextpilot-rag/
├── data/
│   └── raw/
├── src/
│   ├── ingest.py
│   ├── chunk.py
│   ├── embed.py
│   ├── store.py
│   ├── retrieve.py
│   ├── generate.py
│   └── pipeline.py
├── .env.example
├── requirements.txt
└── README.md