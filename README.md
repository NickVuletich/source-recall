# SourceRecall — Local RAG Assistant for Notes, Logs, and Documents

SourceRecall is a local retrieval-augmented generation system for querying messy notes, logs, and documents with source-grounded answers.

The goal of this project is to understand how practical RAG systems work by building the core pipeline piece by piece: document ingestion, text chunking, embeddings, vector storage, semantic retrieval, prompt construction, and local LLM generation.

The project runs locally using ChromaDB, Sentence Transformers, and Ollama. It does not require paid API credits.

## Why I Built This

I built SourceRecall to learn how RAG systems work beyond simple demos. Instead of sending a question directly to an LLM, SourceRecall first retrieves relevant source context from local documents and then uses that context to generate a grounded answer.

This project is intentionally built without hiding the full pipeline behind a large framework. I wanted to understand how data moves through each stage, where retrieval can succeed, and where RAG systems can fail.

The first test data includes fitness logs, business-style notes, and project notes because they are easy to verify. The underlying system is domain-agnostic and can be reused for other local text documents.

## Features

* Loads `.md` and `.txt` documents from `data/raw/`
* Splits documents into overlapping text chunks
* Creates local embeddings using Sentence Transformers
* Stores chunks, embeddings, and metadata in ChromaDB
* Retrieves relevant chunks for a natural language query
* Generates grounded answers with a local Ollama model
* Prints the source documents used for each answer
* Provides a simple CLI workflow for building and querying the local vector store

## Tech Stack

* Python
* ChromaDB
* Sentence Transformers
* Ollama
* Local LLM generation
* Vector search
* Retrieval-Augmented Generation

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
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## How It Works

SourceRecall follows a basic local RAG pipeline:

```txt
raw documents
→ document ingestion
→ text chunking
→ embedding generation
→ ChromaDB vector storage
→ semantic retrieval
→ prompt construction
→ local LLM answer generation
```

When a user asks a question, SourceRecall embeds the query, searches ChromaDB for the most relevant chunks, builds a prompt using the retrieved source context, and sends that prompt to a local Ollama model.

## Setup

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install and run Ollama, then pull a local model:

```bash
ollama pull llama3.2
```

## Usage

Add `.txt` or `.md` files to:

```txt
data/raw/
```

Build the local vector store:

```bash
python src/pipeline.py build
```

Ask a question:

```bash
python src/pipeline.py ask "Which day did I hit a PR?"
```

Whenever documents are added, removed, or edited, rebuild the vector store before asking new questions:

```bash
python src/pipeline.py build
```

## Example Output

Example query:

```bash
python src/pipeline.py ask "Which day did I hit a PR?"
```

Example answer:

```txt
Question:
Which day did I hit a PR?

Answer:
You hit a PR on Day 1.

Sources:
- data/raw/test_day1.txt | distance=1.6272
- data/raw/test_day2.txt | distance=1.7413
- data/raw/test_day6.txt | distance=1.7545
```

## Current Limitations

* The vector store must be rebuilt after adding or editing documents.
* The current chunking approach is character-based, so long documents may split important context across chunks.
* Retrieval only returns the top matching chunks, so aggregate questions may not include every relevant document unless `top_k` is increased.
* RAG is useful for retrieving relevant context, but reliable calculations and statistics require structured extraction.
* The system currently works best with clear `.txt` or `.md` logs.

## Future Improvements

* Add semantic or section-based chunking instead of only character-based chunking
* Add structured extraction for dates, workouts, macros, tasks, and other fields
* Add evaluation tests for retrieval quality and grounded answer accuracy
* Add support for PDFs
* Add a Streamlit or web interface
* Add configurable `top_k` from the command line
* Add better duplicate source handling in output
* Add optional support for multiple document collections

## What I Learned

This project helped me understand that RAG is not just “asking an LLM a question.” A useful RAG system needs a full pipeline around the model: data loading, chunking, embeddings, storage, retrieval, prompt construction, and evaluation.

I also learned that RAG has real limitations. It can retrieve relevant context, but it does not automatically perform reliable full-dataset analysis or calculations unless the system is designed for that. This helped me better understand the difference between semantic retrieval and structured data analysis.

## Status

MVP complete. SourceRecall can build a local vector store from text files, retrieve relevant chunks, and generate grounded answers using a local LLM.
