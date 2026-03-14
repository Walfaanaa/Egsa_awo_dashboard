import openai

openai.api_key = "YOUR_OPENAI_KEY"

def generate_code(question):

    prompt = f"""
You are a Python data analyst.

Dataset columns:
ID
FIRST_NAME
LAST_NAME
MONTHLY_PAYMENT
ADDITIONAL_PAYMENT
EXPENSES_INCURRED
LOAN
punishment
PHONE_NUM

Write pandas code to answer the question.

Return only python code.

Question:
{question}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    code = response["choices"][0]["message"]["content"]

    return code