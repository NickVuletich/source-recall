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