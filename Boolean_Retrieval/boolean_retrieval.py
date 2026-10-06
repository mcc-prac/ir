n = int(input("Enter number of documents: "))

documents = []

for i in range(n):
    doc = input(f"Enter document {i + 1}: ").lower()
    documents.append(doc)

query = input("\nEnter Boolean Query (use AND / NOT): ").lower()

parts = query.split(" not ", 1)
and_part = parts[0].strip()
and_terms = and_part.split()
not_term = parts[1].strip() if len(parts) > 1 else None

all_terms = sorted(
    set(word for doc in documents for word in doc.split())
)

incidence_matrix = {}

print("\nDocument Incidence Matrix (DOM):")
print("Term\t" + "\t".join([f"D{i + 1}" for i in range(n)]))

for term in all_terms:
    row = []
    print(f"{term}\t", end="")

    for doc in documents:
        value = 1 if term in doc.split() else 0
        row.append(value)
        print(f"{value}\t", end="")

    incidence_matrix[term] = row
    print()

query_vectors = []

print("\nQuery term vectors:")

for term in and_terms:
    vector = incidence_matrix.get(term, [0] * n)
    query_vectors.append(vector)
    print(f"{term}: {vector}")

if query_vectors:
    result = query_vectors[0]

    for i in range(1, len(query_vectors)):
        result = [
            result[j] & query_vectors[i][j]
            for j in range(n)
        ]
else:
    result = [0] * n

if not_term:
    if not_term in incidence_matrix:
        not_vector = incidence_matrix[not_term]
        result = [
            result[i] & (1 - not_vector[i])
            for i in range(n)
        ]
    else:
        print(f"\nWarning: NOT term '{not_term}' not found in vocabulary")

print("\nBitwise AND Result:")
print(result)

print("\nRetrieved Documents:")
found = False

for i in range(n):
    if result[i] == 1:
        print(f"D{i + 1}: {documents[i]}")
        found = True

if not found:
    print("No documents satisfy the query.")

# Sample input:
# 3
# information retrieval
# information systems
# retrieval systems
# information NOT systems
