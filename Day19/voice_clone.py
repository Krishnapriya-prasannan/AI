from gtts import gTTS
import os

# Your text to convert to speech
text = "Hello! This is a test for Day 19 of 100 Days of AI."

# Convert text to speech
tts = gTTS(text=text, lang='en')

# Save the output audio
output_file = "day19_speech.mp3"
tts.save(output_file)

# Play the audio using mpg123
os.system(f"mpg123 {output_file}")
