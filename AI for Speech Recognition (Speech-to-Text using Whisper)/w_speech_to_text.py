import whisper
model = whisper.load_model("base")
audio_path = "harvard.wav"
result = model.transcribe(audio_path)
print("Transcription:", result["text"])
with open("transcription.txt", "w") as f:
    f.write(result["text"])
