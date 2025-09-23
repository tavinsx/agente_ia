from agent import AgenteIA

def main():
    """	
    Inicia a aplicação do agente de IA.
    """
    print("seja bem vindo ao corde, seu agente de IA!")

    meu_agente = AgenteIA()

    while True:
        prompt = input("Você: ")

        if prompt.lower() == "sair":
            print("Encerrando a aplicação. Até logo!")
            break


        resposta = meu_agente.enviar_mensagem(prompt)
        print(f"Agente IA: {resposta}")

if __name__ == "__main__":
    main()