import streamlit as st
from src.agent import AgenteIA

st.set_page_config(page_title="Agente de IA", page_icon="🤖")

st.title("🤖 Agente de IA com Google Generative AI")

st.write("Bem-vindo ao seu agente de IA! Digite sua mensagem abaixo e pressione Enter para enviar.")

contexto_inicial = (
    "Você é um agente especializado em desenvolvimento de sites, desenvolvimetos de agentes ias "
    "Responda de forma educada e clara, e sempre pergunte se o usuário precisa de mais ajuda."
    "Você deve responder as perguntas para um aluno de analise e desenvolvimento de sistemas, com um bom conhecimento na area, sempre dando sugestões"
    "Sempre cite exemplos práticos para a aplicação do que está sendo ensinado."
)
meu_agente = AgenteIA(contexto=contexto_inicial)

user_input = st.text_input("Você:", placeholder="Digite sua mensagem aqui...")

if st.button("enviar"):
    if user_input.lower() == "sair":
        st.write("Encerrando a aplicação. Até logo!")
    else:
        resposta = meu_agente.enviar_mensagem(user_input)
        st.write(f"Agente IA: {resposta}")