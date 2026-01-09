import streamlit as st
from main import get_rag_answer, extract_used_sources, formatter

st.set_page_config(page_title="Thesis RAG Chatbot", layout="centered")

st.title("Thesis Chatbot")
st.caption("Ask questions about my master's thesis: \"Performance_Evaluation of Tools for Automatic Processing of Polish L2 Interlanguage\"")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat's history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User's input
question = st.chat_input("Ask a question about the thesis...")

if question:
    # Show the question
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    # RAG
    answer, _, _ = get_rag_answer(question)
    
    # Extract references
    sources = extract_used_sources(answer, formatter)
    
    # Build assistant message
    assistant_content = answer
    
    if sources:
        refs_md = "\n\n---\n**References:**\n"
        for src in sources:
            refs_md += f"- {src}\n"
        assistant_content += refs_md
    
    # Save message
    st.session_state.messages.append(
        {"role": "assistant", "content": assistant_content}
    )
    
    # Display
    with st.chat_message("assistant"):
        st.markdown(assistant_content)
