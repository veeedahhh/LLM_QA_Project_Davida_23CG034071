import openai
import string

openai.api_key = "YOUR_OPENAI_API_KEY"

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

def main():
    print("Welcome to the LLM Q&A CLI!")
    while True:
        question = input("\nEnter your question (or type 'exit' to quit): ")
        if question.lower() == 'exit':
            print("Goodbye!")
            break
        processed_question = preprocess_question(question)
        print(f"Processed Question: {processed_question}")
        answer = ask_llm(processed_question)
        print(f"Answer: {answer}")

if __name__ == "__main__":
    main()
