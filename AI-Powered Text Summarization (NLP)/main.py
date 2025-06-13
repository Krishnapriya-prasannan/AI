from wikipedia_fetcher import get_article_text
from extractive_summarizer import extractive_summary
from abstractive_summarizer import summarize_long_text  

# Step 1: Fetch the article
topic = "Artificial Intelligence"  
article = get_article_text(topic)

# Step 2: Generate extractive summary
print("\nExtractive Summary:\n")
print(extractive_summary(article, n=3))  

# Step 3: Generate abstractive summary
print("\nAbstractive Summary:\n")
print(summarize_long_text(article))  
