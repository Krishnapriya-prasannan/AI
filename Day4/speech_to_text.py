import speech_recognition as sr
recognizer = sr.Recognizer()
with sr.AudioFile("harvard.wav") as source:
    print("Listening...")
    audio = recognizer.record(source)
try:
    text = recognizer.recognize_google(audio)
    print("Transcription:", text)
    with open("output.txt", "w") as f:
        f.write(text)

except sr.UnknownValueError:
    print("Speech not clear.")
except sr.RequestError:
    print("API unavailable or quota exceeded.")
