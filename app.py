import streamlit as st
from src.chat import Chat

st.set_page_config(page_title="Agente de IA", page_icon="🤖")

st.title("🤖 Agente de IA com Google Generative AI")

st.write("Bem-vindo ao seu agente de IA! Digite sua mensagem abaixo e pressione Enter para enviar.")

def main():
    Chat.conversation()

if __name__ == "__main__":
    main()