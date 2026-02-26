from groq import Groq

client = Groq()

chat_completion = client.chat.completions.create(
    messages=[{"role": "user", "content": "How do airplanes fly? Be concise."}],
    model="qwen/qwen3-32b",
    stream=False,
    reasoning_format="parsed",
)

print(chat_completion.choices[0].message)
