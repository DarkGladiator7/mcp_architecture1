# mcp_host/tools/code_explainer_tool.py
import httpx

def code_explainer(code: str) -> str:
    try:
        response = httpx.post("http://localhost:8001/explain", json={"code": code})
        if response.status_code == 200:
            return response.json().get("explanation", "No explanation found.")
        else:
            return f"Error: Received status {response.status_code} from server."
    except Exception as e:
        return f"Code explanation failed: {str(e)}"