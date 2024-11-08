import requests
from ollama import Client  # pip install ollama
import whisper
import os

model = whisper.load_model('small')

def transcrever_audio(audio_path):
    if not os.path.exists(audio_path):
        print(f"Erro: O arquivo de áudio {audio_path} não foi encontrado.")
        return None
    
    audio = whisper.load_audio(audio_path)
    audio = whisper.pad_or_trim(audio)

    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    options = whisper.DecodingOptions(fp16=False)  
 
    result = whisper.decode(model, mel, options)

    return result.text

audio_path = 'test2.m4a'
next1 = transcrever_audio(audio_path)

if next1:
    print(f"Texto transcrito: {next1}")
else:
    print("Falha ao transcrever o áudio.")

def perguntar(questao):
    client = Client(host='http://localhost:11434') 
    model = "llama3.2:3b"
    
    try:
        response = client.chat(model=model, messages=[{"role": "user", "content": questao}])
        return response
    except Exception as e:
        print(f"Erro ao fazer a requisição com Ollama: {e}")
        return None

pergunta = next1 

if pergunta.lower() != "sair": 
    resposta = perguntar(pergunta)

    if resposta:
        try:
            print(f"{resposta['model']}: {resposta['message']['content']}")
        except KeyError as e:
            print(f"Erro ao acessar o conteúdo da resposta: {e}")
    else:
        print("Erro ao obter resposta válida. Tente novamente.")

print("Desligando")
