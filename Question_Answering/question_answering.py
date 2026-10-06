import nltk
from nltk.tokenize import word_tokenize, sent_tokenize

text = """Python is a programming language.
Python was created by Guido van Rossum.
Python is widely used in Artificial Intelligence.
Python was first released in 1991."""

question = input("Enter question: ")

q_words = set(word_tokenize(question.lower()))

best_sentence = ""
best_score = -1

for sentence in sent_tokenize(text):
    words = set(word_tokenize(sentence.lower()))
    score = len(q_words & words)

    if score > best_score:
        best_score = score
        best_sentence = sentence

print("Answer:", best_sentence)

# Sample input:
# When was Python released?
