from collections import defaultdict

n = int(input("Enter the number of documents: "))

documents = {}
for i in range(1, n + 1):
    documents[i] = input(f"Enter Document {i}: ")

term_doc = []

for doc_id, text in documents.items():
    words = text.lower().split()
    for word in words:
        term_doc.append((word, doc_id))

print("-" * 30)
print("{:<15}{}".format("Term", "Doc_ID"))
print("-" * 30)

for term, doc in term_doc:
    print("{:<15}{}".format(term, doc))

sorted_term_doc = sorted(term_doc, key=lambda x: (x[0], x[1]))

print("-" * 30)
print("{:<15}{}".format("Term", "Doc_ID"))
print("-" * 30)

for term, doc in sorted_term_doc:
    print("{:<15}{}".format(term, doc))

posting = defaultdict(set)

for term, doc in sorted_term_doc:
    posting[term].add(doc)

print("-" * 35)
print("{:<15} {}".format("Term", "Doc_Freq"))
print("-" * 35)

for term in sorted(posting):
    print("{:<15}{}".format(term, len(posting[term])))

print("-" * 40)

for term in sorted(posting):
    print(f"{term} -> {sorted(posting[term])}")

# Sample input:
# 2
# Information retrieval
# Information systems
