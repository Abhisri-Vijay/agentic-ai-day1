# Comparing a Plain Chatbot, Rule-Based Workflow, and AI Agent

## 1. Scenario

The selected scenario is a college course fee assistant. The private course fee data is:

- CS101 = ₹12,000
- AI202 = ₹18,000
- DS303 = ₹15,000

The same questions were tested using a plain chatbot, a rule-based workflow, and a tool-using AI agent.

## 2. Objective

The objective is to compare how a plain chatbot, a rule-based workflow, and an AI agent handle private data, calculations, decision-making, flexibility, and multi-step tasks.

## 3.1 Explanation of Each Approach

### Plain Chatbot

The plain chatbot sends the user's question directly to the Large Language Model (LLM). It does not have access to the private course fee data and does not use external tools.

In the test, it could generate a welcome message for new AI students. However, for the course-fee questions, it could not access the actual private data and produced incorrect or uncertain answers.

### Rule-Based Workflow

The rule-based workflow uses predefined Python rules and conditions. It does not use an LLM.

It correctly answered the predefined course-fee questions because the rules directly used the stored course fee data. However, it could not handle the welcome-message question because no rule was created for it.

This shows that a rule-based workflow is reliable for predefined cases but rigid when the question changes.

### AI Agent

The AI agent combines an LLM with tools and a loop.

The agent can decide when it needs information from the course-fee tool and when it needs the calculator. It observes the tool results and uses them to produce the final answer.

For example, for the scholarship question, the agent can retrieve the fees for CS101 and AI202 and then calculate the total after the 10% scholarship.

## 3.2 Comparison

| Feature | Plain Chatbot | Rule-Based Workflow | AI Agent |
|---|---|---|---|
| Uses LLM | Yes | No | Yes |
| Uses private data | No | Yes | Yes through tools |
| Uses tools | No | No | Yes |
| Decision-making | Limited | Predefined rules | LLM-based |
| Flexibility | Higher for conversation | Low | High |
| Handles calculations | May make mistakes | Predefined calculations | Uses calculator tool |
| Handles new tasks | Limited | Poor unless a rule exists | Can select appropriate tools |
| Reliability | May hallucinate | High for predefined rules | Depends on model and tools |
| Multi-step tasks | Limited | Fixed steps only | Can perform multiple tool calls |

## 3.3 Suitability Analysis

### Plain Chatbot

A plain chatbot is suitable for general conversation, text generation, and simple questions that do not require private data or external tools.

### Rule-Based Workflow

A rule-based workflow is suitable when the requirements are fixed and the possible inputs and outputs are clearly defined. It is predictable but requires new rules when new situations occur.

### AI Agent

An AI agent is suitable for tasks that require reasoning, private-data access through tools, calculations, decision-making, and multiple steps. It is more flexible because the LLM can decide which available tool is needed.

## 3.4 Conclusion

The experiment shows that the three approaches work differently.

The plain chatbot is useful for general language tasks but cannot reliably answer questions requiring private data that is not provided to it.

The rule-based workflow can reliably solve predefined problems using fixed rules, but it becomes rigid when a new type of question is introduced.

The AI agent combines an LLM with tools and a loop. It can retrieve private data, perform calculations, observe tool results, and continue the task before giving an answer.

Therefore, the experiment demonstrates the difference between a plain LLM chatbot, a fixed rule-based workflow, and an AI agent based on LLM + Tools + Loop.