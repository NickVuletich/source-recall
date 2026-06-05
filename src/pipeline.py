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