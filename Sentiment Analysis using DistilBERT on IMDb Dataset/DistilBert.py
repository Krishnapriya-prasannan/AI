from datasets import load_dataset
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification, Trainer, TrainingArguments
import torch

# Step 1: Load a SMALL subset of the IMDb dataset to avoid memory issues
dataset = load_dataset("imdb")
train_data = dataset['train'].select(range(2000))  # use only 2000 samples
test_data = dataset['test'].select(range(1000))    # use only 1000 samples

# Step 2: Load the DistilBERT tokenizer
tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased')

# Step 3: Tokenize the data with reduced max_length
def tokenize_function(examples):
    return tokenizer(examples['text'], padding="max_length", truncation=True, max_length=128)

train_data = train_data.map(tokenize_function, batched=True)
test_data = test_data.map(tokenize_function, batched=True)

# Remove the 'text' column
train_data = train_data.remove_columns(["text"])
test_data = test_data.remove_columns(["text"])

# Set the format for PyTorch
train_data.set_format(type="torch", columns=["input_ids", "attention_mask", "label"])
test_data.set_format(type="torch", columns=["input_ids", "attention_mask", "label"])

# Step 4: Load the pretrained DistilBERT model for sequence classification
model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=2)

# Step 5: Define training arguments with safe settings
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=1,                    # Only 1 epoch for safety
    per_device_train_batch_size=4,        # Small batch size
    per_device_eval_batch_size=8,
    warmup_steps=100,
    weight_decay=0.01,
    logging_dir='./logs',
    logging_steps=10,
    evaluation_strategy="epoch",
    save_strategy="epoch",
    save_total_limit=1,
    load_best_model_at_end=False
)

# Step 6: Initialize the Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_data,
    eval_dataset=test_data,
    tokenizer=tokenizer
)

# Step 7: Train the model
trainer.train()

# Step 8: Evaluate the model
results = trainer.evaluate()
print("Evaluation Results:", results)

# Step 9: Save the model and tokenizer
model.save_pretrained('./sentiment_model')
tokenizer.save_pretrained('./sentiment_model')

# Step 10: Making predictions
def predict(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    outputs = model(**inputs)
    prediction = torch.argmax(outputs.logits, dim=-1)
    return "positive" if prediction.item() == 1 else "negative"

# Test with an example
print("Prediction:", predict("I love this movie!"))
