from ollama import Client  # pip install ollama
import fitz  # pip install pymupdf

# Configuração inicial
client = Client(host='http://localhost:11434')  # Sessão persistente para minimizar inicializações
model = "llama3.2:1b"  # Verifique se esse é o modelo correto

# Função para carregar e ler o conteúdo do PDF
def ler_pdf(caminho_pdf):
    texto_completo = ""
    try:
        with fitz.open(caminho_pdf) as pdf:
            for pagina in pdf:
                texto_completo += pagina.get_text()
    except Exception as e:
        print(f"Erro ao ler o PDF: {e}")
    return texto_completo

# Função principal para perguntas e respostas com base no conteúdo do PDF
def perguntar(caminho_pdf, questao):
    # Carrega e lê o conteúdo do PDF
    conteudo_pdf = ler_pdf(caminho_pdf)
    
    if not conteudo_pdf:  # Verifica se o conteúdo do PDF está vazio
        print("Não foi possível ler o conteúdo do PDF. Verifique o arquivo.")
        return

    # Prompt inicial para respostas curtas e claras
    prompt = (
        "Responda com base nas informações a seguir. Mantenha as respostas curtas e claras.\n\n"
        f"Conteúdo:\n{conteudo_pdf}\n\n"
        f"Pergunta: {questao}\nResposta:"
    )

    # Dados para envio ao modelo
    dados = [{"role": "system", "content": prompt}]

    # Conexão em modo streaming
    try:
        print("Enviando pergunta para o modelo...")  # Mensagem de depuração
        stream = client.chat(model=model, stream=True, messages=dados)
        
        # Processa e mostra a resposta em tempo real
        resposta_completa = ''
        for chunk in stream:
            resposta_completa += chunk['message']['content']
            print(chunk['message']['content'], end='', flush=True)
        
        if resposta_completa.strip() == "":
            print("\nNenhuma resposta recebida. Tente fazer uma pergunta diferente.")
        
        print("\n")  # Para melhor formatação das respostas
    except Exception as e:
        print(f"Erro ao gerar resposta: {e}")

# Caminho do PDF
caminho_pdf = "C:\\Users\\Alê\\Desktop\\Projeto\\Fundamentos.pdf"  # Caminho do PDF fornecido
try:
    while True:
        perguntando = input("Você: ")
        if perguntando.lower() == "sair":
            print("Desligando assistente...")
            break

        print("=" * 120)
        print("Pergunta:", perguntando)
        print("=" * 120)
        
        # Chama a função de pergunta com o caminho do PDF e a questão
        perguntar(caminho_pdf, perguntando)
        print("=" * 120)

finally:
    print("Assistente Amy desativada")
