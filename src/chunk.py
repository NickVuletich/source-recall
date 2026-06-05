"""
chunk_text(text, chunk_size=700, overlap=100)
chunk_documents(documents, chunk_size=700, overlap=100)
main()

function chunk_text(text, chunk_size, overlap):
    if chunk_size <= overlap:
        raise ValueError

    create empty list called chunks
    start = 0

    while start is less than length of text:
        end = start + chunk_size
        chunk = text from start to end

        clean whitespace from chunk

        if chunk is not empty:
            append chunk to chunks

        move start forward by chunk_size - overlap

    return chunks
    
function chunk_documents(documents):
    create empty list all_chunks

    for each document:
        chunks = chunk_text(document["text"])

        for each chunk with index:
            create chunk dictionary:
                id = source file + chunk index
                source = document source
                chunk_index = index
                text = chunk text

            append to all_chunks

    return all_chunks
    
"""