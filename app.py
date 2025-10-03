import streamlit as st
from src.chat import Chat
from src.database.db_utils import DBmeneger  

if "db" not in st.session_state:
    st.session_state.db = DBmeneger()


def main():
    st.title("Agente de IA com Busca na Web")
    st.subheader("📥 Adicionar informação na base de conhecimento")
    st.selectbox("Selecione o banco de dados:", options=["base_conhecimento.db"], index=0, key="db_selector")
    user_input = st.text_area("Digite uma informação para salvar no banco:")

    if st.button("Salvar nos conhecimentos"):
        if user_input.strip():
            st.session_state.db.add_content(user_input)
            st.success("Informação salva com sucesso!")
        else:
            st.error("Por favor, digite uma informação válida.")

    Chat.conversation()


if __name__ == "__main__":
    main()
    