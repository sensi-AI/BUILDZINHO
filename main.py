from senha import API_KEY
import requests
import json

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

link = "https://api.openai.com/v1/chat/completions"
id_model = "gpt-3.5-turbo"


prompt = str(input("Texto: "))

requests_body = {
  "model": id_model,
  "messages": [
    {"role": "user", "content": "De acordo com o texto prompt, retorne o sentimento predominante do texto. "
                                "Retorne apenas 'POSITIVE' / 'NEGATIVE' / 'NEUTRAL' ."
                                f"Prompt: f{prompt}"},
  ]
}

requests_body = json.dumps(requests_body)

requisicao = requests.post(link, headers=headers, data=requests_body)
print(requisicao)
print(requisicao.text)

# mostrar o choices
# mostrar o prompt
# mostrar o resultado

resposta = requisicao.json()

mensagem = resposta["choices"][0]["message"]["content"]

print(resposta)
