import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_data
from ai_agent import generate_code  # your AI code generator

# -----------------------------
# Streamlit Page Setup
# -----------------------------
st.set_page_config(layout="wide", page_title="EGSA AI Data Analyst Dashboard")
st.title("EGSA AI Data Analyst Dashboard")

# -----------------------------
# Load Data
# -----------------------------
df = load_data()

if df.empty:
    st.warning("No data available to display.")
else:
    st.subheader("Dataset Preview")
    st.dataframe(df)

    # -----------------------------
    # Ask AI Question
    # -----------------------------
    question = st.text_input("Ask a question about the data")

    if st.button("Analyze") and question.strip():
        try:
            # Generate Python code using AI
            code = generate_code(question)

            st.subheader("Generated Analysis Script")
            st.code(code)

            # -----------------------------
            # Execute AI-generated code safely
            # -----------------------------
            exec_locals = {}
            safe_globals = {"pd": pd, "plt": plt, "df": df}

            exec(code, safe_globals, exec_locals)
            result = exec_locals.get("result", None)

            st.subheader("Result")
            st.write(result)

            # Automatically plot numeric columns if result is a DataFrame
            if isinstance(result, pd.DataFrame):
                numeric_cols = result.select_dtypes(include="number").columns
                if not numeric_cols.empty:
                    st.subheader("Bar Chart of Numeric Columns")
                    st.bar_chart(result[numeric_cols])

        except Exception as e:
            st.error(f"AI code execution failed: {e}")
