import os
from whisper_transcriber import transcrever_audio  
from ollama_model import perguntar  
from text_to_speech import texto_para_audio  
import os



audio_input_folder = './AudioInput'
audio_output_folder = './AudioOutput'

def processar_audios():
    """Função que processa todos os arquivos de áudio na pasta 'AudioInput'"""
    for arquivo in os.listdir(audio_input_folder):
        if arquivo.endswith(('.m4a', '.mp3', '.wav')):
            audio_path = os.path.join(audio_input_folder, arquivo)
            print(f"Processando o arquivo: {audio_path}")
            print(" ")
            
            texto_transcrito = transcrever_audio(audio_path)

            if texto_transcrito:
                print(f"Texto transcrito de {arquivo}: {texto_transcrito}")
                
                resposta = perguntar(texto_transcrito)

                if resposta:
                    print(f"Resposta do modelo para {arquivo}: {resposta}")
                    
                    texto_para_audio(resposta)
                else:
                    print("Erro ao obter resposta do modelo.")
            else:
                print(f"Falha ao transcrever o áudio: {arquivo}")
        else:
            print(f"Arquivo ignorado, não é áudio: {arquivo}")

if __name__ == "__main__":
    processar_audios()
