import requests
import streamlit as st

def get_gemini_response(input_text):
    url = "http://localhost:8000/gemini/invoke"
    payload = {"input":{"product": input_text}}
    response = requests.post(url, json=payload)
    return response.json()['output']['content']

st.title("LangChain Demo With Gemini API")
input_text = st.text_input("Enter your product description here")
if input_text:
    response = get_gemini_response(input_text)
    st.write(response)


