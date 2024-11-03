import whisper

model = whisper.load_model('small')

audio = whisper.load_audio('test2.m4a')
audio = whisper.pad_or_trim(audio)

mel = whisper.log_mel_spectrogram(audio).to(model.device)

options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

print(result.text)