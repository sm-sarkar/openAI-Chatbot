from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Set environment variables (uncomment if needed)
# os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "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"

# Prompt template with a better structure
prompt = ChatPromptTemplate.from_messages(
    [("system", "You are a helpful assistant. Please respond to the user's queries."),
     ("user", "{question}")
    ]
)

# Streamlit framework setup
st.title('LLM ChatBot')
input_text = st.text_input("Search the topic you want.")

# Llama LLM setup
llm = Ollama(model="llama2")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

# Process input and display output
if input_text:
    response = chain.invoke({"question": input_text})
    st.write(response)
