import streamlit as st
from langchain_openai import ChatOpenAI



options = ["gpt-3.5-turbo", "gpt-3.5-turbo-0125", "gpt-4"]
selected_option = st.sidebar.selectbox("Choose a GPT model:", options)
chat_model = ChatOpenAI(model=selected_option, temperature=1)


st.title('Open AI')
question = st.text_input("Ask a question:")
if st.button("Submit") and question:
    response = chat_model.invoke(question)
    st.write("Chatbot:", response)