"""
get_chroma_client(path="chroma_db")
reset_collection(client, collection_name)
build_vector_store()
main()

function get_chroma_client(path):
    create persistent Chroma client at path
    return client
    
function reset_collection(client, collection_name):
    try to delete old collection
    ignore error if collection does not exist

    create new collection
    return collection
    
function build_vector_store():
    load documents
    chunk documents

    if no chunks:
        raise error

    load embedding model
    embed chunk texts

    create Chroma client
    reset/create collection

    prepare:
        ids = chunk ids
        documents = chunk texts
        embeddings = chunk embeddings
        metadatas = source + chunk_index

    add everything to Chroma collection

    return summary:
        document_count
        chunk_count
        collection_name
        
"""