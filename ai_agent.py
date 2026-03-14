import openai

openai.api_key = "YOUR_OPENAI_KEY"

def generate_code(question):
    prompt = f"""
You are a Python data analyst.

Dataset columns:
ID, FIRST_NAME, LAST_NAME, MONTHLY_PAYMENT, ADDITIONAL_PAYMENT, EXPENSES_INCURRED, LOAN, punishment, PHONE_NUM

Write Python pandas code only to answer the question using **only the dataframe `df` and pandas `pd`**.
Do not access files, system, or network.
Return only Python code without explanation.

Question:
{question}
"""
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    code = response["choices"][0]["message"]["content"]

    # Remove possible ```python ``` blocks
    if code.startswith("```"):
        code = "\n".join(code.split("\n")[1:-1])

    return code.strip()
