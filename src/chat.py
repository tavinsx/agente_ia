import streamlit as st
from .agent import AgenteIA
from .storage import Storage
from .ui import render_history


class Chat:
    @staticmethod
    def conversation(conhecimento):
        contexto_inicial = [(
            "Você é um agente especializado em desenvolvimento de sites, desenvolvimetos de agentes ias "
            "Responda de forma educada e clara, e sempre pergunte se o usuário precisa de mais ajuda."
            "Você deve responder as perguntas para um aluno de analise e desenvolvimento de sistemas, com um bom conhecimento na area, sempre dando sugestões"
            "Sempre cite exemplos práticos para a aplicação do que está sendo ensinado."
        )]

        meu_agente = AgenteIA(contexto=contexto_inicial)
        history = Storage.load_history()
        render_history(history)

        if "messages" not in st.session_state:
            st.session_state.messages = []

        for msg in st.session_state.messages:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

        if user_input := st.chat_input("Digite sua mensagem aqui..."):
            st.session_state.messages.append({"role": "user", "content": user_input})
            with st.chat_message("user"):
                st.markdown(user_input)

            resposta = meu_agente.enviar_mensagem(user_input)
            st.session_state.messages.append({"role": "assistant", "content": resposta})
            with st.chat_message("assistant"):
                st.markdown(resposta)

            history.append({"role": "user", "content": user_input})
            history.append({"role": "assistant", "content": resposta})
