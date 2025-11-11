from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

try:
    import streamlit as st
    groq_api_key = st.secrets.get("GROQ_API_KEY")
except:
    groq_api_key = None

# Fallback to .env file if not in Streamlit secrets
if not groq_api_key:
    load_dotenv()
    groq_api_key = os.getenv("GROQ_API_KEY")

if not groq_api_key:
    raise ValueError("GROQ_API_KEY not found in environment variables or Streamlit secrets. Please create a .env file with GROQ_API_KEY=your_key or add it to Streamlit Cloud secrets")
llm = ChatGroq(groq_api_key=groq_api_key, model_name="llama-3.1-8b-instant")


if __name__ == "__main__":
    response = llm.invoke("Two most important ingradient in samosa are ")
    print(response.content)





