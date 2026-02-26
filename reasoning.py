from groq import Groq


client = Groq()
completion = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    messages=[{"role": "user", "content": "How many r's are in the word strawberry?"}],
    temperature=0.6,
    max_completion_tokens=1024,
    top_p=0.95,
    stream=True,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
