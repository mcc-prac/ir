import numpy as np
from sklearn.svm import SVC

n = int(input("Enter number of documents: "))
f = int(input("Enter number of features: "))

if n < 2:
    raise ValueError("At least two documents are required.")

X = []

print("\nEnter features for each document:")

for i in range(n):
    features = list(
        map(
            float,
            input(
                f"Enter {f} features for Document {i + 1}: "
            ).split()
        )
    )

    if len(features) != f:
        raise ValueError(f"Enter exactly {f} features.")

    X.append(features)

X = np.array(X)

y = []

print("\nEnter relevance score for each document:")
print("(Higher value = more relevant)")

for i in range(n):
    score = float(
        input(
            f"Relevance score for Document {i + 1}: "
        )
    )
    y.append(score)

y = np.array(y)

X_pairs = []
y_pairs = []

print("\nPairwise Comparisons:")

for i in range(n):
    for j in range(i + 1, n):

        if y[i] > y[j]:
            print(f"Document {i + 1} > Document {j + 1}")

            X_pairs.append(X[i] - X[j])
            y_pairs.append(1)

            X_pairs.append(X[j] - X[i])
            y_pairs.append(-1)

        elif y[j] > y[i]:
            print(f"Document {j + 1} > Document {i + 1}")

            X_pairs.append(X[j] - X[i])
            y_pairs.append(1)

            X_pairs.append(X[i] - X[j])
            y_pairs.append(-1)

        else:
            print(
                f"Document {i + 1} = Document {j + 1} "
                "(equal relevance; skipped)"
            )

if not X_pairs:
    raise ValueError(
        "No pairwise comparisons were generated. "
        "Use at least two different relevance scores."
    )

X_pairs = np.array(X_pairs)
y_pairs = np.array(y_pairs)

model = SVC(kernel="linear")
model.fit(X_pairs, y_pairs)

weights = model.coef_[0]
scores = X.dot(weights)
ranking = np.argsort(scores)[::-1]

print("\nLearned Weights:", weights)

print("\nFinal Document Ranking:")

for rank, i in enumerate(ranking, start=1):
    print(
        "Rank", rank,
        ": Document", i + 1,
        ": Score =", round(scores[i], 3)
    )

# Sample input:
# 3
# 2
# 1 0
# 0 1
# 1 1
# 3
# 1
# 2
