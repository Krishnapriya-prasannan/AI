from sklearn.model_selection import train_test_split
from load_data import load_dataset

def preprocess_data():
    data = load_dataset()
    data['label'] = data['label'].map({'ham': 0, 'spam': 1})
    X_train, X_test, y_train, y_test = train_test_split(
        data['message'], data['label'], test_size=0.2, random_state=42)
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    preprocess_data()
