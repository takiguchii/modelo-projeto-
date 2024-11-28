from ollama import Client

def perguntar(questao):
    """
    Função que envia uma questão ao modelo Llama e retorna a resposta.
    O modelo é configurado para dar respostas curtas e simples.
    """
    client = Client(host='http://localhost:11434') 
    model = "llama3.2:1b"

    prompt = (
        "Por favor, responda de forma breve, clara e simples. "
        "Evite usar linguagem técnica ou muito detalhada, e procure explicar para que qualquer pessoa possa entender. "
        "Se alguém perguntar sobre um medicamento ou tratamento simples, como para dor de cabeça, forneça opções gerais, como medicamentos comuns para essa condição. "
        "Se a pergunta for sobre algo mais complexo ou sério, informe que não é possível fornecer uma recomendação e que o ideal seria consultar um médico."
    )

    
    mensagem = f"{prompt}\n\nPergunta: {questao}"
    
    try:
        response = client.chat(model=model, messages=[{"role": "user", "content": mensagem}])
        
        return response['message']['content'] if response else None
    except Exception as e:
        print(f"Erro ao fazer a requisição com Ollama: {e}")
        return None

