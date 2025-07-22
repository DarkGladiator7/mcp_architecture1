from fastapi import FastAPI
from pydantic import BaseModel
import httpx

app = FastAPI()

class CodeRequest(BaseModel):
    code: str

class TextRequest(BaseModel):
    text: str

@app.post("/explain-code")
async def explain_code(req: CodeRequest):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8001/explain", json={"code": req.code})
    return response.json()

@app.post("/summarize")
async def summarize_text(req: TextRequest):
    async with httpx.AsyncClient() as client:
        response = await client.post("http://localhost:8002/summarize", json={"text": req.text})
    return response.json()
