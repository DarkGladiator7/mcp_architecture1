# mcp_servers/file_summarizer/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mcp_servers.file_summarizer.service import summarize_text

app = FastAPI(title="MCP Server - File Summarizer")

class TextInput(BaseModel):
    text: str

@app.post("/summarize")
def summarize_endpoint(input: TextInput):
    try:
        result = summarize_text(input.text)
        return {"summary": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
