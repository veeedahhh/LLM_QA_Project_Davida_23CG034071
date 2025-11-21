
import streamlit as st
from openai import OpenAI

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🌟LLM Q&A App")

# User input
user_question = st.text_input("Ask your question:")

# -----------------------------
# OpenAI API function (v1.0+)
# -----------------------------
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])  # Make sure to add your API key in Streamlit Secrets

def ask_llm(question):
    """
    Ask the LLM using OpenAI v1.0+ API.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
            temperature=0.5
        )
        answer = response.choices[0].message.content.strip()
        return answer
    except Exception as e:
        return f"Error: {str(e)}"

# -----------------------------
# Streamlit interaction
# -----------------------------
if user_question:
    with st.spinner("Thinking..."):
        processed_question = user_question
        answer = ask_llm(processed_question)
        st.success(answer)
