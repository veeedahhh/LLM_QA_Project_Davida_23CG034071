import streamlit as st
import openai
import string
import os

# Use environment variable for API key (safer for deployment)
openai.api_key = os.getenv("OPENAI_API_KEY")

def preprocess_question(question):
    question = question.lower()
    question = question.translate(str.maketrans('', '', string.punctuation))
    return question

def ask_llm(question):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=question,
        max_tokens=150,
        temperature=0.5
    )
    return response.choices[0].text.strip()

# Streamlit styling
st.markdown("""
<style>
h1 {color: darkblue; text-align: center;}
div.stTextInput>div>input {background-color: #f0f0f0; padding: 10px;}
div.stButton>button {background-color: darkblue; color: white; padding: 10px 20px;}
</style>
""", unsafe_allow_html=True)

st.title("🌟 NLP Question & Answering System")

user_question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if user_question:
        processed_question = preprocess_question(user_question)
        st.write(f"**Processed Question:** {processed_question}")
        answer = ask_llm(processed_question)
        st.write(f"**Answer:** {answer}")
    else:
        st.write("Please enter a question first!")
