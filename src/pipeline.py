import sys

from store import build_vector_store
from retrieve import retrieve_chunks
from generate import generate_answer

def print_usage():
    print("Available Commands:")
    print("python src/pipeline.py build")
    print('python src/pipeline.py ask "your question"')

def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    command = sys.argv[1]

    if command == "build":
        summary = build_vector_store()

        print("Building SourceRecall vector store...")
        print()
        print(f"Documents: {summary['document_count']}")
        print(f"Chunks: {summary['chunk_count']}")
        print(f"Embeddings: {summary['embedding_count']}")
        print(f"Collection: {summary['collection_name']}")
        print()
        print("Build Complete.")

    elif command == "ask":
        if len(sys.argv) < 3:
            print_usage()
            return
        
        query = " ".join(sys.argv[2:])

        chunks = retrieve_chunks(query, top_k=6)
        answer = generate_answer(query, chunks)

        print("\nQuestion:")
        print(query)

        print("\nAnswer:")
        print(answer)

        print("\nSources:")
        for chunk in chunks:
            source = chunk["metadata"]["source"]
            distance = chunk["distance"]
            print(f"- {source} | distance={distance:.4f}")

    else:
        print("Unknown Command...")
        print_usage()


if __name__ == "__main__":
    main()