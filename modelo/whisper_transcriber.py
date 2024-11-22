import whisper
import os

model = whisper.load_model('small')

def transcrever_audio(audio_path):
    """Função que transcreve o áudio usando o modelo Whisper"""
    if not os.path.exists(audio_path):
        print(f"Erro: O arquivo de áudio {audio_path} não foi encontrado.")
        return None
    
    audio = whisper.load_audio(audio_path)
    audio = whisper.pad_or_trim(audio)

    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    options = whisper.DecodingOptions(fp16=False)  
 
    result = whisper.decode(model, mel, options)

    return result.text
