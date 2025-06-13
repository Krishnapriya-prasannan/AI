from sklearn.feature_extraction.text import TfidfVectorizer
from preprocess_data import preprocess_data

def vectorize_data():
    X_train, X_test, y_train, y_test = preprocess_data()
    vectorizer = TfidfVectorizer()
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    return X_train_tfidf, X_test_tfidf, y_train, y_test, vectorizer

if __name__ == "__main__":
    vectorize_data()
