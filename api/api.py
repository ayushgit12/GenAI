from fastapi import FastAPI
from langchain.prompts import ChatPromptTemplate
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load .env variables
load_dotenv()
google_api_key = os.getenv("GOOGLE_API_KEY")
if not google_api_key:
    raise ValueError("Missing GOOGLE_API_KEY in environment!")

# FastAPI app
app = FastAPI(
    title="GenAI API",
    description="API for GenAI models",
    version="0.1.0"
)

# Model setup
model2 = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    google_api_key=google_api_key
)

# Prompt
prompt2 = ChatPromptTemplate.from_template(
    "What is a good name for a company that makes {product}?"
)

# Add route for Gemini
add_routes(
    app,
    prompt2 | model2,
    path="/gemini"
)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)
