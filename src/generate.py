"""
build_prompt(query, chunks)
generate_answer(query, chunks, model="llama3.2")
main()

function build_prompt(query, chunks):
    create empty context string

    for each chunk:
        add source label
        add chunk text

    create prompt:
        You are SourceRecall.
        Answer only using the context.
        If the answer is not in context, say you do not know.
        Context: ...
        Question: ...
        Answer:

    return prompt
    
function generate_answer(query, chunks, model):
    prompt = build_prompt(query, chunks)

    send prompt to Ollama model

    get response text

    return response text
    
read query from command line
retrieve chunks
generate answer
print answer
print sources

python src/generate.py "Which day did I hit a PR?"

"""