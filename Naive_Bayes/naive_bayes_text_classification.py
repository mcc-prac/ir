from collections import Counter

texts = [
    "good excellent amazing",
    "great wonderful good",
    "excellent fantastic good",
    "amazing wonderful excellent",
    "bad terrible boring",
    "awful boring bad",
    "terrible disappointing bad",
    "boring awful terrible"
]

labels = [
    "Positive", "Positive", "Positive", "Positive",
    "Negative", "Negative", "Negative", "Negative"
]

vocabulary = set()

for text in texts:
    vocabulary.update(text.lower().split())

positive_texts = []
negative_texts = []

for i in range(len(texts)):
    if labels[i] == "Positive":
        positive_texts.append(texts[i])
    else:
        negative_texts.append(texts[i])

total_documents = len(texts)

positive_prior = len(positive_texts) / total_documents
negative_prior = len(negative_texts) / total_documents

print("--- PRIOR PROBABILITY ---")
print("P(Positive) =", round(positive_prior, 4))
print("P(Negative) =", round(negative_prior, 4))

positive_words = []
negative_words = []

for text in positive_texts:
    positive_words.extend(text.lower().split())

for text in negative_texts:
    negative_words.extend(text.lower().split())

positive_count = Counter(positive_words)
negative_count = Counter(negative_words)

total_positive_words = len(positive_words)
total_negative_words = len(negative_words)
vocab_size = len(vocabulary)


def probability(word, word_count, total_words):
    return (word_count[word] + 1) / (total_words + vocab_size)


print("\n--- CONDITIONAL PROBABILITY ---")

for word in sorted(vocabulary):
    p_positive = probability(
        word,
        positive_count,
        total_positive_words
    )
    p_negative = probability(
        word,
        negative_count,
        total_negative_words
    )

    print(
        word,
        ": P(word|Positive) =",
        round(p_positive, 4),
        ", P(word|Negative) =",
        round(p_negative, 4)
    )

test_text = input("\nEnter a review: ")
test_words = test_text.lower().split()

positive_probability = positive_prior
negative_probability = negative_prior

for word in test_words:
    if word in vocabulary:
        positive_probability *= probability(
            word,
            positive_count,
            total_positive_words
        )
        negative_probability *= probability(
            word,
            negative_count,
            total_negative_words
        )

print("\n--- NAIVE BAYES RESULT ---")
print(
    "P(Positive | Text) =",
    round(positive_probability, 6)
)
print(
    "P(Negative | Text) =",
    round(negative_probability, 6)
)

print("\n--- FINAL PREDICTION ---")

if positive_probability > negative_probability:
    print("Prediction: Positive")
else:
    print("Prediction: Negative")

# Sample input:
# good amazing
