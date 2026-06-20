from agent import client


def evaluate_response(query, context, response_text):

    evaluation_prompt = f"""
    You are an AI evaluator.

    Question:
    {query}

    Retrieved Context:
    {context}

    Generated Response:
    {response_text}

    Evaluate the response on:

    1. Relevance (1-5)
    2. Accuracy (1-5)
    3. Completeness (1-5)
    4. Groundedness (1-5)

    Return output in this format:

    Relevance: X/5
    Accuracy: X/5
    Completeness: X/5
    Groundedness: X/5

    Overall Score: X/5

    Justification:
    <short explanation>
    """

    evaluation = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": evaluation_prompt
            }
        ]
    )

    return evaluation.choices[0].message.content