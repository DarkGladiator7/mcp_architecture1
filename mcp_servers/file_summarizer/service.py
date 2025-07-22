import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

# Load environment variables
load_dotenv()

# Initialize LLM
llm = init_chat_model("llama3-8b-8192", model_provider="groq")

# Core function: summarize extracted text from file
def summarize_text(text: str) -> str:
    prompt = f"""Summarize the following content in a concise and clear paragraph:\n\n{text}"""

    response = llm.invoke(prompt)
    return response.content.strip()
