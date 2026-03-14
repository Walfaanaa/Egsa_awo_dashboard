import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from data_loader import load_data
from ai_agent import generate_code

st.set_page_config(layout="wide")

st.title("EGSA AI Data Analyst Dashboard")

# Load data
df = load_data()

st.subheader("Dataset Preview")
st.dataframe(df)

question = st.text_input("Ask a question about the data")

if st.button("Analyze"):

    code = generate_code(question)

    st.subheader("Generated Analysis Script")
    st.code(code)

    try:

        result = eval(code)

        st.subheader("Result")
        st.write(result)

        if isinstance(result, pd.DataFrame):

            st.bar_chart(result)

    except Exception as e:

        st.error("AI code execution failed")