# agente_ia

O **agente_ia** é um agente de inteligência artificial desenvolvido para auxiliar alunos e profissionais de Análise e Desenvolvimento de Sistemas. Ele utiliza o modelo Google Generative AI (Gemini) para responder perguntas, sugerir exemplos práticos e apoiar o aprendizado em desenvolvimento de sites e agentes inteligentes.

## Tecnologias Utilizadas

- [Google Generative AI (Gemini)](https://ai.google.dev/)
- [Python](https://www.python.org/)
- [Streamlit](https://streamlit.io/) (interface web)
- [python-dotenv](https://pypi.org/project/python-dotenv/) (gestão de variáveis de ambiente)

## Funcionalidades

- Respostas inteligentes e contextualizadas para dúvidas técnicas
- Sugestões práticas e exemplos de aplicação
- Interface de linha de comando (CLI)
- Interface web interativa via Streamlit
- Extensível para novos módulos e integrações

## Instalação

Clone o repositório:

```bash
git clone https://github.com/seuusuario/agente_ia.git
cd agente_ia
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

## Configuração

Crie um arquivo `.env` na raiz do projeto e adicione sua chave da API do Google Generative AI:

```
GOOGLE_API_KEY=seu_token_aqui
```

## Uso

### Linha de Comando (CLI)

Execute o agente via terminal:

```bash
python src/main.py
```

Digite suas perguntas e interaja com o agente. Para encerrar, digite `sair`.

### Interface Web

Execute a interface web com Streamlit:

```bash
streamlit run app.py
```

Acesse o endereço exibido no terminal para interagir via navegador.

## Contribuição

Contribuições são bem-vindas! Para sugerir melhorias, abra uma issue ou envie um pull request.

## Licença

Este projeto está sob a licença MIT.
