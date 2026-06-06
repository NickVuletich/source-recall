"""
build
ask

create Typer app

command build:
    call build_vector_store()
    print summary

command ask(query, top_k=3):
    retrieve chunks using query
    generate answer using query + chunks
    print answer
    print sources
    
python src/pipeline.py build
python src/pipeline.py ask "What did I eat on June 1?"

"""

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
        print(summary)

    elif command == "ask":
        if len(sys.argv) < 3:
            print_usage()
            return
        
        query = " ".join(sys.argv[2:])

        chunks = retrieve_chunks(query)
        answer = generate_answer(query, chunks)

        print(answer)
        for chunk in chunks:
            print(chunk["metadata"]["source"])

    else:
        print("Unknown Command...")
        print_usage()


if __name__ == "__main__":
    main()