import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from collections import Counter

text = """Artificial Intelligence is changing the world.
Machine learning is an important part of artificial intelligence.
AI is used in healthcare and education.
AI helps computers learn from data."""

sentences = sent_tokenize(text)

words = word_tokenize(text.lower())
freq = Counter(words)

scores = {}

for sentence in sentences:
    sentence_words = word_tokenize(sentence.lower())
    scores[sentence] = sum(
        freq[word] for word in sentence_words
    )

summary = sorted(
    sentences,
    key=lambda x: scores[x],
    reverse=True
)[:2]

print("Summary:")
print(" ".join(summary))

# Sample input:
# text = """Artificial intelligence helps computers learn from data.
# Machine learning is used in healthcare and education."""
