import math
from collections import Counter

n = int(input("Enter number of documents: "))

documents = []

for i in range(n):
    doc = input(f"Enter Document {i + 1}: ").lower()
    documents.append(doc)

query = input("Enter Query: ").lower()

doc_tokens = [doc.split() for doc in documents]
query_tokens = query.split()

print("\n----- TERM FREQUENCY TABLE -----")

for i, tokens in enumerate(doc_tokens):
    freq = Counter(tokens)
    print(f"\nDocument {i + 1}:")
    for term, count in freq.items():
        print(f"  {term}: {count}")

query_freq = Counter(query_tokens)

print("\nQuery:")
for term, count in query_freq.items():
    print(f"  {term}: {count}")

vocabulary = set()

for tokens in doc_tokens:
    vocabulary.update(tokens)

vocabulary.update(query_tokens)
vocabulary = sorted(vocabulary)

print("\n----- SORTED VOCABULARY -----")
print(vocabulary)

print("\n----- DOCUMENT TF VECTORS -----")

doc_tf_vectors = []

for i, tokens in enumerate(doc_tokens):
    freq = Counter(tokens)
    vector = [freq.get(term, 0) for term in vocabulary]
    doc_tf_vectors.append(vector)
    print(f"Document {i + 1}: {vector}")

query_tf_vector = [query_freq.get(term, 0) for term in vocabulary]

print("\nQuery TF Vector:")
print(query_tf_vector)

idf = {}

for term in vocabulary:
    document_frequency = sum(
        1 for tokens in doc_tokens if term in tokens
    )
    idf[term] = math.log(n / document_frequency) if document_frequency else 0.0

print("\n----- IDF VALUES -----")

for term in vocabulary:
    print(f"{term}: {idf[term]:.4f}")

doc_tfidf_vectors = []

print("\n----- DOCUMENT TF-IDF VECTORS -----")

for i, tf_vector in enumerate(doc_tf_vectors):
    vector = [
        tf * idf[term]
        for tf, term in zip(tf_vector, vocabulary)
    ]
    doc_tfidf_vectors.append(vector)
    print(f"Document {i + 1}: {[round(x, 4) for x in vector]}")

query_tfidf_vector = [
    tf * idf[term]
    for tf, term in zip(query_tf_vector, vocabulary)
]

print("\nQuery TF-IDF Vector:")
print([round(x, 4) for x in query_tfidf_vector])


def cosine_similarity(v1, v2):
    dot_product = sum(a * b for a, b in zip(v1, v2))
    magnitude_v1 = math.sqrt(sum(a * a for a in v1))
    magnitude_v2 = math.sqrt(sum(b * b for b in v2))

    if magnitude_v1 == 0 or magnitude_v2 == 0:
        return 0.0

    return dot_product / (magnitude_v1 * magnitude_v2)


print("\n----- COSINE SIMILARITY -----")

similarities = []

for i, vector in enumerate(doc_tfidf_vectors):
    sim = cosine_similarity(vector, query_tfidf_vector)
    similarities.append((i + 1, sim))
    print(f"Document {i + 1}: {sim:.4f}")

ranked_docs = sorted(
    similarities,
    key=lambda x: x[1],
    reverse=True
)

# Sample input:
# 2
# information retrieval
# retrieval systems
# information

print("\n----- RANKED DOCUMENTS -----")

for rank, (doc_id, sim) in enumerate(ranked_docs, start=1):
    print(
        f"Rank {rank}: Document {doc_id} "
        f"(Similarity = {sim:.4f})"
    )
