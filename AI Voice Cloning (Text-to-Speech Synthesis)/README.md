
### **AI Voice Cloning (Text-to-Speech Synthesis)**

As part of my **#100DaysOfAI** challenge, on **Day 19**, I explored the fascinating world of **Text-to-Speech (TTS)** by generating human-like speech from **plain text** using AI-powered models.

---

### **Goal**

Convert **natural language text** into **realistic speech audio**, mimicking a human voice using AI-driven text-to-speech synthesis.

---

### **Technologies Used**

| Tool/Library | Purpose                                                   |
|--------------|------------------------------------------------------------|
| Python       | Core programming language                                  |
| `gTTS`       | Google Text-to-Speech – simple text-to-MP3 conversion      |
| `mpg123`     | Lightweight MP3 player for audio playback on Linux         |
| `os`         | To execute command-line instructions to play the audio     |

---

### **How It Works**

1. **Install Required Packages**
   - Installed `gTTS` using pip.
   - Installed `mpg123` via apt for playing the output audio.

2. **Convert Text to Speech**
   - Used `gTTS` to process a sample string and save it as an MP3 audio file.

3. **Play the Audio**
   - Played the generated speech using the `mpg123` command in the terminal.

---

### **Highlights**

- Created a **fully functional AI-powered speech generator** in just a few lines of code.
- Ran the entire pipeline **offline with local tools**, except for the API call by gTTS.
- Explored **TTS concepts** used in smart assistants, screen readers, and accessibility tools.
- Understood the difference between simple TTS (like gTTS) and advanced models (like Tacotron or Coqui TTS).

---

### **What I Learned**

- How easy it is to implement **basic voice synthesis** using gTTS.
- The importance of tools like `mpg123` for **playing audio on Linux systems**.
- Practical applications of TTS in **IVR systems, accessibility software**, and **virtual assistants**.
- The potential of more advanced models like **Tacotron 2, Coqui TTS**, and **Real-Time Voice Cloning** for building custom voice AI.

---

