
### **Day 16 - Sentiment Analysis using DistilBERT on IMDb Dataset**  
As part of my **#100DaysOfAI** challenge, on **Day 16**, I fine-tuned a **DistilBERT** model on the **IMDb movie reviews dataset** to classify sentiments as **positive** or **negative**. This exercise introduced me to transfer learning with pre-trained Transformers using Hugging Face’s `transformers` and `datasets` libraries.

---

### **Goal**  
Fine-tune a pre-trained **DistilBERT** model for **binary sentiment classification** on the IMDb dataset and understand the end-to-end process of training, evaluating, and using Transformer-based models.

---

### **Technologies Used**

| Tool/Library       | Purpose                                                      |
|--------------------|--------------------------------------------------------------|
| Python             | Core programming language                                    |
| Hugging Face Datasets | To load and preprocess the IMDb dataset                 |
| Hugging Face Transformers | Tokenizer, pretrained model, Trainer API           |
| PyTorch            | Deep learning backend for training and predictions           |
| DistilBERT         | Lightweight Transformer model used for text classification   |

---

### **How It Works**

1. **Data Preparation**
   - Loaded the IMDb dataset using `load_dataset()`.
   - Tokenized text reviews using `DistilBertTokenizerFast` with padding and truncation.

2. **Model Selection**
   - Used `DistilBertForSequenceClassification` with 2 output labels (positive/negative).
   - Initialized model with weights from `distilbert-base-uncased`.

3. **Training Setup**
   - Defined `TrainingArguments` for controlling epochs, batch size, evaluation steps, etc.
   - Used Hugging Face’s `Trainer` to handle training and evaluation seamlessly.

4. **Model Training**
   - Trained the model for **1 epoch** with a reduced dataset for resource efficiency.
   - Evaluated on a held-out test set to measure accuracy.

5. **Making Predictions**
   - Created a `predict()` function to classify new reviews.
   - Saved the fine-tuned model and tokenizer locally for reuse.

---

### **Highlights**

- Fine-tuned **DistilBERT** for a real-world NLP task (sentiment analysis).
- Handled **tokenization, padding, and truncation** of variable-length inputs.
- Applied **Trainer API** for quick training and evaluation with minimal code.
- Understood how to save and reuse fine-tuned models for inference.
- Successfully performed sentiment predictions on custom user inputs.

---

### **What I Learned**

- The power of **transfer learning** with pre-trained Transformer models.
- How **tokenization** and **input formatting** affect model performance.
- The role of `Trainer` and `TrainingArguments` in simplifying model training.
- Optimizing batch sizes and input length to fit training on low-resource machines.
- Built a complete **sentiment analysis pipeline** using DistilBERT and PyTorch.

---

