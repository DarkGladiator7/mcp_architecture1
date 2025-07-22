from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from mcp_servers.code_explainer.service import explain_code

app = FastAPI(title="MCP Server - Code Explainer")

class CodeInput(BaseModel):
    code: str

@app.post("/explain")
def explain_endpoint(input: CodeInput):
    try:
        result = explain_code(input.code)
        return {"explanation": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))