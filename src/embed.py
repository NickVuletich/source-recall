from sentence_transformers import SentenceTransformer
from ingest import load_documents
from chunk import chunk_documents

def load_embedding_model(model_name="all-MiniLM-L6-v2"):
    model = SentenceTransformer(model_name)
    return model

def embed_texts(texts, model):
    embeddings = model.encode(texts)
    embeddings = embeddings.tolist()
    return embeddings

if __name__ == "__main__":
    model = load_embedding_model()

    documents = load_documents("data/raw")
    chunks = chunk_documents(documents)

    texts = [chunk["texts"] for chunk in chunks]

    embeddings = embed_texts(texts, model)

    print(f"Documents loaded: {len(documents)}")
    print(f"Chunks created: {len(chunks)}")
    print(f"Embeddings created: {len(embeddings)}")
    print(f"Embedding dimension: {len(embeddings[0])}")

