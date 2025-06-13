from gtts import gTTS
import os

# Your text to convert to speech
text = "Hello! This is a test ."

# Convert text to speech
tts = gTTS(text=text, lang='en')

# Save the output audio
output_file = "speech.mp3"
tts.save(output_file)

# Play the audio using mpg123
os.system(f"mpg123 {output_file}")
