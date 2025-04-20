
### **Day 8 - AI-Powered Text Summarization (NLP)**  
This is part of my **#100DaysOfAI** challenge.  
On **Day 8**, I implemented an AI-powered **text summarization system** using **Natural Language Processing (NLP)** techniques — both **extractive** and **abstractive** summarization models.

---

### **Goal**  
Summarize long articles into concise and meaningful summaries using extractive and abstractive approaches.

---

### **Technologies Used**

| Tool             | Purpose                                       |
|------------------|-----------------------------------------------|
| Python           | Main programming language                     |
| Hugging Face Transformers | Pre-trained models for abstractive summarization |
| NLTK             | Tokenization and extractive text processing   |
| Wikipedia        | Source for long-form articles                 |
| VS Code          | Code editor                                   |

---

### **Dataset / Input**  
- Any **Wikipedia article** fetched live using the `wikipedia` Python package.  
- Example topic: `"Artificial Intelligence"`

---

### **How It Works**

1. **Wikipedia Fetching**  
   - Used the `wikipedia` library to fetch article content based on a topic.

2. **Extractive Summarization** (`extractive_summary.py`)  
   - Tokenized text into sentences and words using NLTK.
   - Calculated word frequencies and sentence scores.
   - Selected top-N most informative sentences as the summary.

3. **Abstractive Summarization** (`abstractive_summarizer.py`)  
   - Used Hugging Face's `facebook/bart-large-cnn` model for summarization.
   - Split long text into smaller chunks.
   - Summarized each chunk and combined them for a coherent summary.

4. **Main Script** (`main.py`)  
   - Combined all components.
   - Printed both **extractive** and **abstractive** summaries for the given article.

---

### **Highlights**

- Compared **extractive** (rule-based) vs. **abstractive** (AI-generated) summaries.
- Used **state-of-the-art NLP models** from Hugging Face.
- Applied **text chunking** to handle long articles with token limits.
- Fetched real-world data from **Wikipedia** dynamically.

---

### **What I Learned**

- The difference between **extractive** and **abstractive** summarization.
- How to use **Hugging Face Transformers** for summarization tasks.
- How to break down long texts into manageable chunks for better processing.
- Real-world text preprocessing using NLTK.
- End-to-end integration of NLP tools for practical AI applications.

---

