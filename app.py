
import streamlit as st
import openai

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("🌟LLM Q&A App")

# User input
user_question = st.text_input("Ask your question:")

# -----------------------------
# OpenAI API function
# -----------------------------
def ask_llm(question):
    """
    Ask the LLM using the new ChatCompletion API.
    """
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": question}
            ],
            temperature=0.5,
        )
        # Extract the assistant's reply
        answer = response.choices[0].message['content'].strip()
        return answer

    except Exception as e:
        return f"Error: {str(e)}"

# -----------------------------
# Streamlit interaction
# -----------------------------
if user_question:
    with st.spinner("Thinking..."):
        processed_question = user_question  # Keep any preprocessing you had
        answer = ask_llm(processed_question)
        st.success(answer)
