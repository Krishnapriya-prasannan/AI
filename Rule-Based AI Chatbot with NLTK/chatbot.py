import nltk
nltk.download('punkt')
nltk.download('punkt_tab')   
from nltk.tokenize import word_tokenize

def chatbot_response(user_input):
    tokens = word_tokenize(user_input.lower())

    if "hello" in tokens or "hi" in tokens:
        return "Hey there! Need any help?"
    elif "weather" in tokens:
        return "I can't check the weather yet, but I'm working on it!"
    elif "name" in tokens:
        return "I'm AI-Bot, your assistant."
    elif "bye" in tokens or "exit" in tokens:
        return "Goodbye!"
    else:
        return "I'm not sure how to respond to that."

while True:
    user = input("You: ")
    if user.lower() in ['bye', 'exit']:
        print("AI-Bot:", chatbot_response(user))
        break
    
    print("AI-Bot:", chatbot_response(user))

