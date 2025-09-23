from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser 

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["OPENAI_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"

# Prompt template
prompt = ChatPromptTemplate.from_messages(
     [
          ("system", "You are a helpful assistant. Please respond to the user queries "),
          ("user", "Question: {question}"),
     ]
)


# Streamlit Framework
st.title("Langchain Demo With OPENAI")
input_text = st.text_input("Enter your question here")

# openai llm
llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser
if input_text:
     response = chain.invoke({"question": input_text})
     st.write(response)

