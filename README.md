# MCP Architecture - Modular AI Tooling

## Overview
This project demonstrates a modular AI system using the MCP (Model-Client-Server) architecture. It supports:
- Code explanation using LLMs
- File summarization from uploaded .txt, .md, or .pdf files

All components are decoupled and communicate via HTTP.

## Project Structure
- mcp_host: Streamlit frontend with LangChain agent and tools
- mcp_client: FastAPI-based middleware that routes requests
- mcp_servers:
  - code_explainer: FastAPI service to explain Python code
  - file_summarizer: FastAPI service to summarize file content

## Setup Instructions

1. Clone the repository:
   git clone https://github.com/DarkGladiator7/mcp_architecture.git
   cd mcp_architecture

2. Create and activate a virtual environment:
   python -m venv venv
   venv\Scripts\activate   (Windows)
   source venv/bin/activate   (macOS/Linux)

4. Install dependencies:
   pip install -r requirements.txt

5. Create a .env file in the root directory and add:
   GROQ_API_KEY=your_groq_key
   

## How to Run

Open four terminals and run each of the following:

Terminal 1 - Code Explainer Server:
   uvicorn mcp_servers.code_explainer.main:app --reload --port 8001

Terminal 2 - File Summarizer Server:
   uvicorn mcp_servers.file_summarizer.main:app --reload --port 8002

Terminal 3 - MCP Client:
   uvicorn mcp_client.main:app --reload --port 8000

Terminal 4 - MCP Host (UI):
   streamlit run mcp_host/main.py

## Features
- Paste code for explanation in the UI
- Upload .txt, .md, or .pdf files for summarization
