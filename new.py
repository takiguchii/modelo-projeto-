import pygame
from gtts import gTTS
import os

def dividir_texto(texto, limite=100): 
    return [texto[i:i+limite] for i in range(0, len(texto), limite)]

def texto_para_audio():
    texto = input("Digite o texto que deseja transformar em áudio: ")
    
    partes_texto = dividir_texto(texto)
    
    pasta_audio = "audios"
    
    if not os.path.exists(pasta_audio):
        os.makedirs(pasta_audio)
    
    pygame.mixer.init()

    for i, parte in enumerate(partes_texto):
        tts = gTTS(text=parte, lang='pt')
        
        arquivo_audio = os.path.join(pasta_audio, f"audio_{i}.mp3")
        
        tts.save(arquivo_audio)
        
        print(f"Reproduzindo a parte {i + 1}... Arquivo salvo em {arquivo_audio}")
        
        # Carregar e reproduzir a parte do áudio
        pygame.mixer.music.load(arquivo_audio)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

texto_para_audio()
