from sklearn.naive_bayes import MultinomialNB
from tfidf_vectorizer import vectorize_data

def train_model():
    X_train_tfidf, X_test_tfidf, y_train, y_test, vectorizer = vectorize_data()
    model = MultinomialNB()
    model.fit(X_train_tfidf, y_train)
    return model, X_test_tfidf, y_test, vectorizer

if __name__ == "__main__":
    train_model()
