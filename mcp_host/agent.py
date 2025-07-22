# mcp_host/agent.py

from langchain.agents import initialize_agent, Tool
from langchain.chat_models import init_chat_model

from tools.code_explainer_tool import code_explainer
from tools.file_summarizer_tool import file_summarizer
import os 
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq LLM using langchain
llm = init_chat_model("llama3-8b-8192", model_provider="groq")

def create_agent():
    tools = [
        Tool(
            name="Code Explainer",
            func=code_explainer,  # this now sends HTTP request to MCP client
            description="Use this tool to explain code snippets.",
        ),
        Tool(
            name="File Summarizer",
            func=file_summarizer,  # this now sends HTTP request to MCP client
            description="Use this tool to summarize uploaded text or PDF files.",
        ),
    ]

    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent="zero-shot-react-description",
        verbose=True,
    )
    return agent
