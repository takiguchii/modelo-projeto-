from ollama import Client  

def perguntar(questao):
    client = Client(host='http://localhost:11434') 
    model = "llama3.2"
    
    try:
        response = client.chat(model=model, messages=[{"role": "user", "content": questao}])
        return response['message']['content'] if response else None
    except Exception as e:
        print(f"Erro ao fazer a requisição com Ollama: {e}")
        return None
