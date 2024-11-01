import requests
import os

print("Iniciando Assistente")

prompt_personalizado = (
    "Responda de forma clara e objetiva. "
    "Evite discutir sobre assuntos que não são referentes a farmácia, como carros e tal. "
    "Concentre-se em fornecer informações apenas sobre farmácia e nada mais que isto. "
    "Gere respostas simples e fáceis de entender, e evite respostas longas."
)

pergunta = "Qual é o medicamento para dor de cabeça?"

url = "http://localhost:11434/api/chat"
data = {
    "model": "llama3.2",  # Usando o modelo 3.2
    "messages": [
        {"role": "system", "content": prompt_personalizado},  # Mudando para 'system' para diretrizes
        {"role": "user", "content": pergunta}
    ],
    "stream": False
}

response = requests.post(url, json=data)
os.system('cls')
print("Pergunta:", pergunta)
print(" ")

# Guardando a resposta em uma variável
resposta = response.json().get('message', {}).get('content', 'Sem resposta')
print("Resposta:", resposta)

# Aqui você pode adicionar a chamada para o código que converte a resposta em áudio
# Exemplo:
# converter_audio(resposta)

print("Desligando")
