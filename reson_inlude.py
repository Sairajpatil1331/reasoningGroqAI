from groq import Groq

client = Groq()

chat_completion = client.chat.completions.create(
    messages=[{"role": "user", "content": "How do airplanes fly? Be concise."}],
    model="openai/gpt-oss-20b",
    reasoning_effort="high",
    include_reasoning=True,
    stream=False,
)

print(chat_completion.choices[0].message)
