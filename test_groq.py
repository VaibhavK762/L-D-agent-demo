from agent import client

response = client.chat.completions.create(
    model="llama-3.3-70b-versatile",
    messages=[
        {
            "role": "user",
            "content": "What is machine learning?"
        }
    ]
)

print(response.choices[0].message.content)