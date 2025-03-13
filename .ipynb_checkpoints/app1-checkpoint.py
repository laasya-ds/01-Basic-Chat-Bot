# GOOGLE_API_KEY = "AIzaSyAVoyYyqNgmjZANCh5XtE4y6a-Ix6L_6cs"
from dotenv import load_dotenv
load_dotenv()

import streamlit as st
import os
import google.generativeai as genai

genai.configure(api_key="AIzaSyAVoyYyqNgmjZANCh5XtE4y6a-Ix6L_6cs")

model = genai.GenerativeModel("gemini-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text

### Initialize streamlit app
st.set_page_config(page_title = "Q&A Demo")
st.header("Chat with me")
input=st.text_input("Input: ", key="input")
submit=st.button("Enter")

if submit:
    response=get_gemini_response(input)
    st.subheader("Response")
    st.write(response)