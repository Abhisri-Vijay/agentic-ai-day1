from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

model = os.getenv("MODEL")

questions = [
    "What is the fee for AI202?",
    "What is the total fee for CS101 and AI202 after a 10% scholarship?",
    "Is DS303 more expensive than CS101, and by how much?",
    "Write a two-line welcome message for new AI students."
]

for question in questions:
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "user", "content": question}
        ]
    )

    print("\nQuestion:", question)
    print("Answer:", response.choices[0].message.content)