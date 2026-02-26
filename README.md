Reasoning


Reasoning models excel at complex problem-solving tasks that require step-by-step analysis, logical deduction, and structured thinking and solution validation. With Groq inference speed, these types of models can deliver instant reasoning capabilities critical for real-time applications.

Why Speed Matters for Reasoning
Reasoning models are capable of complex decision making with explicit reasoning chains that are part of the token output and used for decision-making, which make low-latency and fast inference essential. Complex problems often require multiple chains of reasoning tokens where each step build on previous results. Low latency compounds benefits across reasoning chains and shaves off minutes of reasoning to a response in seconds.

Supported Models
Model ID	Model
openai/gpt-oss-20b

OpenAI GPT-OSS 20B
openai/gpt-oss-120b

OpenAI GPT-OSS 120B
openai/gpt-oss-safeguard-20b

OpenAI GPT-OSS-Safeguard 20B
qwen/qwen3-32b

Qwen 3 32B

Reasoning Effort
Options for Reasoning Effort (Qwen 3 32B)
The reasoning_effort parameter controls the level of effort the model will put into reasoning. This is only supported by Qwen 3 32B.

reasoning_effort Options	Description
none	Disable reasoning. The model will not use any reasoning tokens.
default	Enable reasoning.
Options for Reasoning Effort (GPT-OSS)
The reasoning_effort parameter controls the level of effort the model will put into reasoning. This is only supported by GPT-OSS 20B and GPT-OSS 120B.

reasoning_effort Options	Description
low	Low effort reasoning. The model will use a small number of reasoning tokens.
medium	Medium effort reasoning. The model will use a moderate number of reasoning tokens.
high	High effort reasoning. The model will use a large number of reasoning tokens.
