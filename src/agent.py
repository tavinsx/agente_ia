import google.generativeai as genai
import os
from dotenv import load_dotenv


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
        model = genai.GenerativeModel("gemini-1.5-flash-latest")

        history = []
        if contexto: 
            history = [
                   {
                       "role": "user",
                       "parts": [
                           {"text": "Olá, tudo bem?"}
                       ]
                   },
                   {
                       "role": "model",
                       "parts": [
                           {"text": "Tudo ótimo! E você?"}
                       ]
                   }
                ]

        self.chat = model.start_chat(history=history)
        print("Agente IA iniciado! Digite 'sair' para encerrar.")

    def enviar_mensagem(self, prompt):
        """
        envia mensagem do usuário e retorna a resposta do agente.
        """
        try:
            response = self.chat.send_message(prompt)

            if response and response.candidates:
                resposta_formatada = response.candidates[0].content.parts[0].text
            print(response)
            return resposta_formatada
        except Exception as e:
            return f"Erro ao enviar mensagem: {e}"


