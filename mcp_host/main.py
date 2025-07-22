# mcp_host/main.py

import streamlit as st
from agent import create_agent
from tools.file_summarizer_tool import file_summarizer

st.set_page_config(page_title="MCP Host", layout="wide")
st.title("🧠 MCP Host (LangChain Agent Interface)")

# Initialize agent only once
if "agent" not in st.session_state:
    st.session_state.agent = create_agent()

# Tabs
tab1, tab2 = st.tabs(["💬 Code Explanation", "📄 File Summarization"])

# --- Tab 1: Code Explanation ---
with tab1:
    st.subheader("Code Explanation")
    query = st.text_area("Enter your code or question:", height=200, key="code_input")

    if st.button("Run Agent", key="code_button"):
        if query.strip():
            with st.spinner("Thinking..."):
                result = st.session_state.agent.run(query)
            st.subheader("Explanation:")
            st.write(result)
        else:
            st.warning("Please enter a valid code prompt.")

# --- Tab 2: File Summarization ---
with tab2:
    st.subheader("File Summarization")
    uploaded_file = st.file_uploader("Upload a .txt, .md, or .pdf file", type=["txt", "md", "pdf"], key="file_input")

    if st.button("Summarize File", key="file_button"):
        if uploaded_file:
            with st.spinner("Summarizing file..."):
                result = file_summarizer(uploaded_file)
            st.subheader("Summary:")
            st.write(result)
        else:
            st.warning("Please upload a valid file.")
