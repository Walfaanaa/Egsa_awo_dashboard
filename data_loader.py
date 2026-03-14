import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from ai_agent import generate_code  # your AI code generator

# -----------------------------
# Load Data from local CSV
# -----------------------------
@st.cache_data
def load_data():
    try:
        df = pd.read_csv("AWO.csv")  # make sure this file is in the same folder as your app
        return df
    except Exception as e:
        st.error(f"Failed to load CSV locally: {e}")
        return pd.DataFrame()  # empty dataframe on failure

df = load_data()

# -----------------------------
# Streamlit Layout
# -----------------------------
st.set_page_config(layout="wide")
st.title("EGSA AI Data Analyst Dashboard")

st.subheader("Dataset Preview")
st.dataframe(df)

question = st.text_input("Ask a question about the data")

if st.button("Analyze"):
    code = generate_code(question)
    st.subheader("Generated Analysis Script")
    st.code(code)

    # -----------------------------
    # Safe execution of AI code
    # -----------------------------
    exec_locals = {}
    try:
        # Only allow pandas, matplotlib, and the dataframe
        safe_globals = {"pd": pd, "plt": plt, "df": df}
        exec(code, safe_globals, exec_locals)
        result = exec_locals.get("result", None)

        st.subheader("Result")
        st.write(result)

        # If DataFrame, show bar chart for numeric columns
        if isinstance(result, pd.DataFrame):
            numeric_cols = result.select_dtypes(include='number').columns
            if not numeric_cols.empty:
                st.bar_chart(result[numeric_cols])

    except Exception as e:
        st.error(f"AI code execution failed: {e}")
