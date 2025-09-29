import streamlit as st



def render_history(history: list):
    for msg in history:
        role = "🧑 Usuário" if msg["role"] == "user" else "🤖 IA"
        st.markdown(f"**{role}:** {msg['content']}")