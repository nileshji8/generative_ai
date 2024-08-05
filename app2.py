from dotenv import load_dotenv
load_dotenv()  # Load all environment variables

import streamlit as st
import os
import google.generativeai as genai

# Configure the API key for google.generativeai
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Function to load the generative model and get responses
model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response = model.generate_content(question)
    return response.text

# Initialize our Streamlit app
st.set_page_config(page_title="Q&A Demo", page_icon=":robot:", layout="centered")

# Title and description
st.title("Gemini LLM Application")
st.write(
    """
    Welcome to the Gemini LLM Q&A Application! 
    Ask any question and get a response from the powerful Gemini language model.
    """
)

# User input
input = st.text_input("Input:", key="input", placeholder="Type your question here...")
submit = st.button("Ask the Question")
clear = st.button("Clear Input")

# Container for responses
response_container = st.container()

# When submit is clicked
if submit:
    if input:
        with st.spinner('Generating response...'):
            try:
                response = get_gemini_response(input)
                with response_container:
                    st.write("### Response:")
                    st.write(response)
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a question before submitting.")

# When clear is clicked
if clear:
    st.session_state.input = " "
    response_container.empty()

# Footer
st.markdown(
    """
    ---
    **Developed by NIHAL KUMAR MISHRA**
    """
)

# Adding some style to the app
st.markdown(
    """
    <style>
    .main {
        background-color: #f5f5f5;
        padding: 20px;
        border-radius: 10px;
    }
    .title {
        color: #4B8BBE;
        font-family: 'Arial';
        font-size: 36px;
    }
    .footer {
        text-align: center;
        font-size: 12px;
        color: #888888;
    }
    .css-1cpxqw2 {
        padding: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
