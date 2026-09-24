from data.course_fees import COURSE_FEES


def rule_based_answer(question):
    q = question.lower()

    if "fee for ai202" in q:
        return "AI202 fee is ₹18,000."

    elif "total fee" in q and "cs101" in q and "ai202" in q:
        total = COURSE_FEES["CS101"] + COURSE_FEES["AI202"]
        final_fee = total * 0.90
        return f"Total fee after 10% scholarship is ₹{final_fee:.0f}."

    elif "ds303" in q and "cs101" in q and "more expensive" in q:
        difference = COURSE_FEES["DS303"] - COURSE_FEES["CS101"]
        return f"Yes, DS303 is more expensive by ₹{difference}."

    else:
        return "No rule available for this question."


questions = [
    "What is the fee for AI202?",
    "What is the total fee for CS101 and AI202 after a 10% scholarship?",
    "Is DS303 more expensive than CS101, and by how much?",
    "Write a two-line welcome message for new AI students."
]

for question in questions:
    print("\nQuestion:", question)
    print("Answer:", rule_based_answer(question))