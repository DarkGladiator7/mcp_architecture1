import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# Load environment variables
load_dotenv()

# Initialize LLM
llm = init_chat_model("llama3-8b-8192", model_provider="groq")

# Core function: take code, return plain English explanation
def explain_code(code: str) -> str:
    prompt = f"""You are a helpful assistant. Explain the following code in plain English:\n\n{code}"""
    
    response = llm.invoke(prompt)
    return response.content.strip()
