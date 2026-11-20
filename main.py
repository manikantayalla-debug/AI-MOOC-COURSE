from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

my_model = os.getenv("OLLAMA_MODEL")
my_base_url = os.getenv("OLLAMA_BASE_URL")
my_api_key = os.getenv("OLLAMA_API_KEY")

ollama = OpenAI(base_url=my_base_url,api_key=my_api_key)

response = ollama.chat.completions.create(model=my_model,
messages=[{"role":"user","content":"What is 2 + 2?"}])

print(response.choices[0].message.content)