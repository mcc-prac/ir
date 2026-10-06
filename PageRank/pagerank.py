import numpy as np

n = int(input("Enter the number of nodes (webpages): "))
e = int(input("Enter the number of links: "))
iterations = int(input("Enter the number of iterations: "))

adj = np.zeros((n, n))

print("\nEnter the links (From To):")
print("(Example: 1 2 means Page 1 links to Page 2)")

for i in range(e):
    u, v = map(int, input(f"Link {i + 1}: ").split())

    if not (1 <= u <= n and 1 <= v <= n):
        raise ValueError("Node numbers must be between 1 and n.")

    adj[v - 1][u - 1] = 1

M = np.zeros((n, n))

for j in range(n):
    out_degree = np.sum(adj[:, j])

    if out_degree != 0:
        M[:, j] = adj[:, j] / out_degree
    else:
        M[:, j] = 1 / n

print("\nTransition Matrix (M):")
print(M)

r = np.ones(n) / n

print("\nInitial Rank Vector (r0):")
print(r)

for i in range(iterations):
    r = np.dot(M, r)

    print(f"\nr{i + 1}:")
    print(r)

highest = np.argmax(r)

print("\nFinal PageRank Values:")

for i in range(n):
    print(f"Node {i + 1}: {r[i]:.4f}")

print(f"\nNode with Highest PageRank: Node {highest + 1}")
print(f"Highest PageRank Value: {r[highest]:.4f}")

print("\nPageRank computation completed successfully.")

# Sample input:
# 3
# 3
# 5
# 1 2
# 2 3
# 3 1
