from openai import OpenAI

OLLAMA_BASE_URL = "http://localhost:11434/v1"
ollama = OpenAI(base_url=OLLAMA_BASE_URL, api_key='ollama')

system_prompt = """
You are a fun fact generator.
You are given a topic and you need to generate a fun fact about it.
"""

user_prompt = """
Tell me a fun fact about the topic of AI.
"""

response = ollama.chat.completions.create(model="deepseek-r1:1.5b", messages=[
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
])

print(response.choices[0].message.content)