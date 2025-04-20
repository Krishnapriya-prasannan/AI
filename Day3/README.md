
# Day 3 - AI-Powered Spam Detector

This project is part of my **#100DaysOfAI** challenge. On **Day 3**, I built a simple AI model that classifies SMS messages as **Spam** or **Not Spam** using Natural Language Processing and Machine Learning techniques.

---

## Project Goal

- Learn how AI can be used for **text classification**
- Build a spam detection model using **Naive Bayes**
- Understand and implement **TF-IDF** for feature extraction
- Evaluate the model and predict on custom input

---

## Technologies Used

| Tool / Library     | Purpose                                  |
|--------------------|-------------------------------------------|
| **Python**         | Core programming language                 |
| **Scikit-learn**   | Machine learning & NLP tools              |
| **Pandas**         | Data loading and processing               |
| **TF-IDF**         | Convert text to numeric form              |
| **VS Code**        | Code editor used                         |

---

## Dataset Used

- **SMS Spam Collection Dataset**  
  Source: [UCI ML Repository](https://archive.ics.uci.edu/ml/datasets/SMS+Spam+Collection)  
  File: `SMSSpamCollection`

---

## How It Works

1. **Load Data**  
   Load SMS messages and labels (`ham`, `spam`) from a text file.

2. **Preprocess Text**  
   Clean and convert data into a format suitable for training.

3. **TF-IDF Vectorization**  
   Convert text into numerical features using TF-IDF.

4. **Train Naive Bayes Model**  
   A probabilistic classifier is trained to distinguish spam from ham.

5. **Evaluate Accuracy**  
   The model is tested on unseen messages for performance.

6. **Custom Prediction**  
   Input your own SMS messages to test whether they are spam or not.

---


