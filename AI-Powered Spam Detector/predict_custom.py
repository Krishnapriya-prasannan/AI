from train_model import train_model

def predict_custom_message(msg):
    model, _, _, vectorizer = train_model()
    msg_vector = vectorizer.transform([msg])
    prediction = model.predict(msg_vector)
    return "Spam" if prediction[0] == 1 else "Not Spam"

if __name__ == "__main__":
    print(predict_custom_message("Congratulations! You’ve won a free iPhone. Click now!"))
    print(predict_custom_message("Hey, are we meeting tomorrow?"))
