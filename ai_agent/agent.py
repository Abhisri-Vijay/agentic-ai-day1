from openai import OpenAI
from dotenv import load_dotenv
from ai_agent.tools import get_course_fee, calculate
import os
import json

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url=os.getenv("OPENAI_BASE_URL")
)

model = os.getenv("MODEL")

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_course_fee",
            "description": "Get the fee of a course using its course code.",
            "parameters": {
                "type": "object",
                "properties": {
                    "course_code": {
                        "type": "string"
                    }
                },
                "required": ["course_code"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "calculate",
            "description": "Calculate a mathematical expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string"
                    }
                },
                "required": ["expression"]
            }
        }
    }
]

questions = [
    "What is the fee for AI202?",
    "What is the total fee for CS101 and AI202 after a 10% scholarship?",
    "Is DS303 more expensive than CS101, and by how much?",
    "Write a two-line welcome message for new AI students."
    "I can pay ₹30,000. Which two courses can I take together within this budget?"
]

system_prompt = """
You are a college fee assistant.

You have access to private course fee data through tools.
Never guess course fees.

Use get_course_fee whenever a course fee is needed.
Use calculate whenever arithmetic is needed.
Answer the user only after getting the required information.
"""

for question in questions:

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question}
    ]

    print("\nQuestion:", question)

    for step in range(5):

        response = client.chat.completions.create(
            model=model,
            messages=messages,
            tools=tools,
            tool_choice="auto"
        )

        message = response.choices[0].message

        if message.tool_calls:
            messages.append(message)

            for tool_call in message.tool_calls:
                name = tool_call.function.name
                args = json.loads(tool_call.function.arguments)

                print("Tool:", name)
                print("Arguments:", args)

                if name == "get_course_fee":
                    result = get_course_fee(args["course_code"])

                elif name == "calculate":
                    result = calculate(args["expression"])

                print("Result:", result)

                messages.append({
                    "role": "tool",
                    "tool_call_id": tool_call.id,
                    "content": str(result)
                })

        else:
            print("Answer:", message.content)
            break