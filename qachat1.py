from dotenv import load_dotenv
load_dotenv()  # Call load_dotenv with parentheses

import streamlit as st
import os
import google.generativeai as genai

st.set_page_config(page_title="Q&A Demo")

st.header("Gemini LLM Application")  # Use single string for header

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## FUNCTION TO LOAD GEMINI-PRO MODEL AND GET RESPONSE

model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

## Initialize our Streamlit app

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

user_input = st.text_input("Input:", key="input")  # Use descriptive variable name
submit = st.button("Ask the question")

if submit and user_input:
    response = get_gemini_response(user_input)
    ## Add user query and response to session chat history
    st.session_state['chat_history'].append(("You", user_input))
    st.subheader("The Response is")
    for chunk in response:
        st.write(chunk.text)
        st.session_state['chat_history'].append(("Bot", chunk.text))

st.subheader("The Chat history is")

for role, text in st.session_state['chat_history']:
    st.write(f"{role}: {text}")  # Add space after colon
