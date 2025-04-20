import pandas as pd

def load_dataset():
    data = pd.read_csv("SMSSpamCollection", sep="\t", header=None, names=["label", "message"])
    print("Sample Data:\n", data.head())
    return data

if __name__ == "__main__":
    load_dataset()
