import networkx as nx
import numpy as np

n = int(input("Enter number of nodes: "))
m = int(input("Enter number of edges: "))
itr = int(input("Enter number of iterations: "))

G = nx.DiGraph()
G.add_nodes_from(range(n))

print("Enter edges (u v):")
print(f"Use node numbers from 0 to {n - 1}.")

for _ in range(m):
    u, v = map(int, input().split())

    if not (0 <= u < n and 0 <= v < n):
        raise ValueError("Node numbers must be between 0 and n-1.")

    G.add_edge(u, v)

authority = np.ones(n)
hub = np.ones(n)

for k in range(itr):
    new_authority = np.zeros(n)

    for node in range(n):
        for pred in G.predecessors(node):
            new_authority[node] += hub[pred]

    norm_authority = np.linalg.norm(new_authority)

    if norm_authority != 0:
        new_authority = new_authority / norm_authority

    new_hub = np.zeros(n)

    for node in range(n):
        for succ in G.successors(node):
            new_hub[node] += new_authority[succ]

    norm_hub = np.linalg.norm(new_hub)

    if norm_hub != 0:
        new_hub = new_hub / norm_hub

    authority = new_authority
    hub = new_hub

    print(f"\nIteration {k + 1}")
    print("Node\tAuthority\tNorm Authority\tHub\tNorm Hub")

    for i in range(n):
        print(
            f"{i}\t{new_authority[i]:.3f}\t\t"
            f"{norm_authority:.3f}\t\t"
            f"{new_hub[i]:.3f}\t{norm_hub:.3f}"
        )

print(
    "\nBest Authority Node:",
    np.argmax(authority),
    "Score:",
    round(float(max(authority)), 3)
)

print(
    "Best Hub Node:",
    np.argmax(hub),
    "Score:",
    round(float(max(hub)), 3)
)

# Sample input:
# 3
# 3
# 5
# 0 1
# 1 2
# 2 0
