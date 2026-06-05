"""
load_embedding_model(model_name="all-MiniLM-L6-v2")
embed_texts(texts, model)
main()

function load_embedding_model(model_name):
    load SentenceTransformer model
    return model
    
function embed_texts(texts, model):
    pass list of texts into model.encode()
    convert output to normal Python list
    return embeddings
    
load documents
chunk documents
load embedding model
collect chunk["text"] into a list
embed those texts
print number of embeddings
print embedding dimension

"""
from sentence_transformers import SentenceTransformer
from ingest import load_documents

def load_embedding_model(model_name="all-MiniLM-L6-v2"):
    model = SentenceTransformer(model_name)
    return model

def embed_texts(texts, model):
    embeddings = model.encode(texts)
    embeddings = embeddings.to_list()
    return embeddings

if __name__ == "__main__":
    model = load_embedding_model()

    texts = [
        "protein was 185 grams today",
        "bench press felt strong"
    ]

    embeddings = embed_texts(texts, model)

    print(len(embeddings))
    print(len(embeddings[0]))
