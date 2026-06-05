# SourceRecall — Local RAG Assistant for Notes, Logs, and Documents

SourceRecall is a local retrieval-augmented generation system for querying messy notes, logs, and documents.

The goal is to learn how RAG systems work by building the pipeline piece by piece: document ingestion, chunking, embeddings, vector storage, retrieval, prompt construction, local LLM generation, and basic evaluation.

The first test data uses fitness logs because they are easy to verify, but the system is designed to be reusable across other domains like business notes, project documentation, client records, and internal workflow data.

## Why I Built This

I built SourceRecall to understand how practical RAG systems work beyond demos. Instead of only calling an LLM directly, this project retrieves relevant source context first, then uses that context to generate grounded answers.

This project is intentionally built without hiding the whole pipeline behind a large framework. I want to understand how the data moves through each stage and where RAG systems can succeed or fail.

## Features

* Load `.md` and `.txt` documents from `data/raw/`
* Split documents into overlapping text chunks
* Create local embeddings using Sentence Transformers
* Store chunks in ChromaDB
* Retrieve relevant chunks for a natural language query
* Generate grounded answers with a local Ollama model
* Print source chunks used in the answer

## Tech Stack

* Python
* ChromaDB
* Sentence Transformers
* Ollama
* Typer
* Rich

## Project Structure

```txt
source-recall/
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
```
