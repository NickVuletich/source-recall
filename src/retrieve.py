"""
retrieve_chunks(query, top_k=3)
main()

function retrieve_chunks(query, top_k):
    connect to existing ChromaDB
    get collection

    load same embedding model
    embed the user query

    ask Chroma for top_k closest chunks

    create empty retrieved list

    for each result:
        create dictionary:
            id
            text
            metadata
            distance

        append to retrieved list

    return retrieved
    
read query from command line
call retrieve_chunks(query)
print each result:
    source
    distance
    preview text
    
python src/retrieve.py "Which day did I hit a PR?"
python src/retrieve.py "What was my protein intake?"
python src/retrieve.py "Which day was a rest day?"
"""