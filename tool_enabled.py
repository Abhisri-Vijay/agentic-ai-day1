from openai import OpenAI
from dotenv import load_dotenv
from ai_agent.tools import get_course_fee
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
            "description": "Get the private fee of a course using its course code.",
            "parameters": {
                "type": "object",
                "properties": {
                    "course_code": {
                        "type": "string",
                        "description": "The course code, such as CS101, AI202, or DS303."
                    }
                },
                "required": ["course_code"]
            }
        }
    }
]

questions = [
    "What is the fee for AI202?",
    "What is the fee for DS303?",
    "Write a two-line welcome message for new AI students."
]

system_prompt = """
You are a college course fee assistant.

Private course fee information is available through the get_course_fee tool.

Use get_course_fee whenever the user asks for a course fee.
Never guess or invent course fees.

If the question does not require course fee information, answer normally without using the tool.
"""

for question in questions:

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": question}
    ]

    print("\n" + "=" * 60)
    print("Question:", question)

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

            print("Tool Call:", name)
            print("Arguments:", args)

            if name == "get_course_fee":
                result = get_course_fee(args["course_code"])
            else:
                result = "Tool not found."

            print("Tool Result:", result)

            messages.append({
                "role": "tool",
                "tool_call_id": tool_call.id,
                "content": str(result)
            })

        final_response = client.chat.completions.create(
            model=model,
            messages=messages
        )

        print("Final Answer:", final_response.choices[0].message.content)

    else:
        print("Tool Call: None")
        print("Final Answer:", message.content)