from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

response = client.chat.completions.create(
    model=os.getenv("MODEL"),
    messages=[
        {"role": "user", "content": "Reply with exactly: SETUP OK"}
    ]
)

print(response.choices[0].message.content)