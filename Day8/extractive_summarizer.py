# extractive_summarizer.py

import nltk
from nltk.tokenize import sent_tokenize
from heapq import nlargest
from collections import defaultdict

nltk.download("punkt")

def extractive_summary(text, n=5):
    sentences = sent_tokenize(text)
    word_freq = defaultdict(int)

    for word in nltk.word_tokenize(text.lower()):
        if word.isalpha():
            word_freq[word] += 1

    sentence_scores = {}
    for sent in sentences:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_freq:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + word_freq[word]

    top_sentences = nlargest(n, sentence_scores, key=sentence_scores.get)
    return " ".join(top_sentences)
