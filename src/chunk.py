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

from ingest import load_documents

def chunk_text(text, chunk_size=700, overlap=100):
    if chunk_size <= overlap:
        raise ValueError("chunck_size must be greater than overlap")

    chunks = []
    start = 0

    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunk = chunk.strip()

        if chunk:
            chunks.append(chunk)
        start += chunk_size - overlap
    return chunks

def chunk_documents(documents):
    all_chunks = []

    for doc in documents:
        chunks = chunk_text(doc["text"])

        for index, chunk in enumerate(chunks):
            chunk_dict = ({
                "id": f"{doc['source']}::chunk-{index}",
                "source": doc["source"],
                "chunk_index": index, 
                "text": chunk,
            })
            all_chunks.append(chunk_dict)

    return all_chunks

if __name__ == "__main__":
    documents = load_documents("data/raw")
    chunks = chunk_documents(documents)

    print(f"Loaded documents: {len(documents)}")
    print(f"Created chunks: {len(chunks)}")

    for chunk in chunks:
        print(chunk["id"])
        print(chunk["text"][:200])