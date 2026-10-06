import matplotlib.pyplot as plt

relevant_input = input(
    "Enter relevant documents (space separated): "
)
relevant_documents = set(relevant_input.split())

retrieved_input = input(
    "Enter retrieved documents in ranked order: "
)
retrieved_documents = retrieved_input.split()

total_relevant = len(relevant_documents)
relevant_count = 0

precision_values = []
recall_values = []
ranks = []

print("\nPrecision-Recall Table")
print("-" * 65)
print("Rank\tDocument\tRelevant\tPrecision\tRecall")
print("-" * 65)

for rank, document in enumerate(retrieved_documents, start=1):
    if document in relevant_documents:
        relevant_count += 1

    precision = (relevant_count / rank) * 100

    if total_relevant > 0:
        recall = (relevant_count / total_relevant) * 100
    else:
        recall = 0.0

    ranks.append(rank)
    precision_values.append(precision)
    recall_values.append(recall)

    print(
        rank,
        "\t", document,
        "\t", relevant_count,
        "\t", round(precision, 2), "%",
        "\t", round(recall, 2), "%"
    )

print("\nPrecision-Recall Points:")

for i in range(len(ranks)):
    print(
        "(",
        round(recall_values[i], 2),
        ",",
        round(precision_values[i], 2),
        ")"
    )

if relevant_count > 0:
    final_precision = precision_values[-1]
    final_recall = recall_values[-1]

    print(
        "\nFinal Precision =",
        round(final_precision, 2),
        "%"
    )
    print(
        "Final Recall =",
        round(final_recall, 2),
        "%"
    )

if precision_values:
    plt.plot(
        recall_values,
        precision_values,
        marker="o"
    )
    plt.xlabel("Recall (%)")
    plt.ylabel("Precision (%)")
    plt.title("Precision-Recall Curve")
    plt.grid(True)
    plt.show()

# Sample input:
# D1 D3
# D2 D1 D3
