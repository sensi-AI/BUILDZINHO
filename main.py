from senha import API_KEY
import requests
import json
from time import sleep

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

link = "https://api.openai.com/v1/chat/completions"
id_model = "gpt-3.5-turbo"


def sentiment_analysis(texto):

    requests_body = {
        "model": id_model,
        "messages": [
            {"role": "user", "content": "De acordo com o texto prompt, retorne o sentimento predominante do texto. "
                                        "Retorne apenas 'POSITIVO' / 'NEGATIVO' / 'NEUTRO' ."
                                        f"Prompt: f{texto}"},
        ]
    }

    requests_body = json.dumps(requests_body)

    requisicao = requests.post(link, headers=headers, data=requests_body)

    resposta = requisicao.json()

    mensagem = resposta["choices"][0]["message"]["content"]

    return mensagem


prompt = str(input("Texto: "))

print(sentiment_analysis(prompt))


