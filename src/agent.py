import google.generativeai as genai  # type: ignore
import os
from dotenv import load_dotenv
 # type: ignore


class AgenteIA:
    """
    Classe que representa um agente de IA capaz de interagir com o usuário e realizar buscas na web.
    """
    def __init__(self, contexto=None):
        """
        Inicializa o agente com a chave da API do Google Generative AI.
        """
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError("A chave da API do Google Generative AI não foi encontrada nas variáveis de ambiente.")
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("models/gemini-2.5-flash")
     

        self.initial_history = []
        if contexto:
            self.initial_history = [
                {'role': 'user', 'parts': [contexto]},
                {'role': 'model', 'parts': ["Entendido. Serei seu assistente e seguirei essas instruções."]}
            ]

        self.chat = model.start_chat(history=self.initial_history)
        print("Agente IA iniciado! Digite 'sair' para encerrar.")

    def enviar_mensagem(self, prompt):
    
        try:
            response = self.chat.send_message(prompt)

            if response and response.candidates:
                resposta_formatada = response.candidates[0].content.parts[0].text
                return resposta_formatada
        except Exception as e:
            return f"Erro ao enviar mensagem: {e}"


