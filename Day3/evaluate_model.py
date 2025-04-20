from sklearn.metrics import accuracy_score, classification_report
from train_model import train_model

def evaluate():
    model, X_test_tfidf, y_test, _ = train_model()
    y_pred = model.predict(X_test_tfidf)
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))

if __name__ == "__main__":
    evaluate()
