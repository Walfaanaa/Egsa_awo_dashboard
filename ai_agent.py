import openai

# Replace with your actual OpenAI API key
openai.api_key = "YOUR_OPENAI_KEY"

def generate_code(question):
    """
    This function takes a natural language question and uses OpenAI to
    generate Python pandas code to analyze the dataset `df`.
    """

    # The prompt we give to OpenAI
    prompt = f"""
You are a Python data analyst.

Dataset columns:
ID, FIRST_NAME, LAST_NAME, MONTHLY_PAYMENT, ADDITIONAL_PAYMENT, EXPENSES_INCURRED, LOAN, punishment, PHONE_NUM

Write Python pandas code only to answer the question using the dataframe `df` and pandas `pd`.
Return only Python code, no explanation.

Question:
{question}
"""

    # -----------------------------
    # This is where ChatCompletion is called
    # -----------------------------
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    # Extract the Python code returned by the AI
    code = response["choices"][0]["message"]["content"]

    # Remove triple backticks if present
    if code.startswith("```"):
        code = "\n".join(code.split("\n")[1:-1])

    return code.strip()
