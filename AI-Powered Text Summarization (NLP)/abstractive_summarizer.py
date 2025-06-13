# abstractive_summarizer.py

from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def split_text(text, max_len=1000):
    return [text[i:i+max_len] for i in range(0, len(text), max_len)]

def summarize_long_text(text):
    chunks = split_text(text)
    final_summary = ""
    for chunk in chunks:
        summary_chunk = summarizer(chunk, max_length=130, min_length=30, do_sample=False)[0]['summary_text']
        final_summary += summary_chunk + " "
    return final_summary
