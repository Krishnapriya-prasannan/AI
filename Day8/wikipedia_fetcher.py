# wikipedia_fetcher.py

import wikipedia

def get_article_text(topic="Artificial intelligence"):
    return wikipedia.page(topic).content
