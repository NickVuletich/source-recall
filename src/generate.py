import ollama
from retrieve import retrieve_chunks

def build_prompt(query, chunks):
    context_blocks = []

    for chunk in chunks:
        source = chunk["metadata"]["source"]
        text = chunk["text"]

        context_block = f"[Source: {source}]\n{text}"
        context_blocks.append(context_block)

    context_string = "\n\n".join(context_blocks)

    prompt = f"""
You are SourceRecall, a local RAG assistant.

Answer the user's question using only the provided context.
If the answer is not in the context, say you do not have enough information.

Context:
{context_string}

Question:
{query}

Answer:
""".strip()
    
    return prompt


def generate_answer(query, chunks, model_name="llama3.2"):
    prompt = build_prompt(query, chunks)

    response = ollama.generate(
        model=model_name,
        prompt=prompt,
    )

    return response["response"]


if __name__ == "__main__":
    query = "Which day did I hit a PR?"
    chunks = retrieve_chunks(query)

    answer = generate_answer(query, chunks)
    print(answer)

