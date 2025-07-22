# mcp_host/tools/file_summarizer_tool.py

import httpx
import fitz  # PyMuPDF
import markdown
import os

def extract_text_from_file(file) -> str:
    filename = file.name.lower()

    if filename.endswith(".pdf"):
        with fitz.open(stream=file.read(), filetype="pdf") as doc:
            text = ""
            for page in doc:
                text += page.get_text()
            return text.strip()

    elif filename.endswith(".md"):
        raw = file.read().decode("utf-8")
        html = markdown.markdown(raw)
        return html  # or use `BeautifulSoup(html).text` if needed

    elif filename.endswith(".txt"):
        return file.read().decode("utf-8").strip()

    else:
        raise ValueError("Unsupported file type.")

def file_summarizer(uploaded_file) -> str:
    try:
        extracted_text = extract_text_from_file(uploaded_file)
        if not extracted_text:
            return "No readable text found in the uploaded file."
        print(extracted_text)  # Debugging line to check extracted text

        response = httpx.post("http://localhost:8000/summarize", json={"text": extracted_text})
        if response.status_code == 200:
            return response.json().get("summary", "No summary returned.")
        else:
            return f"Error: Server responded with {response.status_code}"
    except Exception as e:
        return f"File summarizer failed: {str(e)}"
