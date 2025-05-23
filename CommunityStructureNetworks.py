# Unit-IV Community structure in networks: Communities and community detection in networks, Hierarchical algorithms for community detection, Modularity based community detection algorithms, Label Propagation algorithm.

import networkx as nx
import matplotlib.pyplot as plt
import community.community_louvain as community_louvain
from networkx.algorithms import community as nx_comm

def draw_communities(G, partition, title):
    pos = nx.spring_layout(G, seed=42)
    colors = [partition[node] for node in G.nodes()]
    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_color=colors, cmap=plt.cm.Set3, node_size=800, edge_color='gray')
    plt.title(title)
    plt.show()

# Generate a synthetic graph with community structure
G = nx.karate_club_graph()  # Classic benchmark graph
print("=== Karate Club Graph Loaded ===")

# 1. Louvain Method (Modularity-based community detection)
print("\n--- Modularity-Based (Louvain) ---")
partition_louvain = community_louvain.best_partition(G)
draw_communities(G, partition_louvain, "Louvain Modularity-Based Communities")
modularity_score = community_louvain.modularity(partition_louvain, G)
print("Modularity Score:", modularity_score)

# 2. Girvan-Newman (Hierarchical / Edge Betweenness)
print("\n--- Hierarchical (Girvan-Newman) ---")
comp = nx_comm.girvan_newman(G)
limited = tuple(sorted(c) for c in next(comp))  # First level of hierarchy
partition_gn = {}
for idx, community in enumerate(limited):
    for node in community:
        partition_gn[node] = idx
draw_communities(G, partition_gn, "Girvan-Newman Hierarchical Communities")

# 3. Label Propagation Algorithm
print("\n--- Label Propagation ---")
label_prop = nx_comm.label_propagation_communities(G)
partition_lp = {}
for i, com in enumerate(label_prop):
    for node in com:
        partition_lp[node] = i
draw_communities(G, partition_lp, "Label Propagation Communities")

# Summary
print("\nCommunity Sizes:")
print("Louvain:", {v: list(partition_louvain.values()).count(v) for v in set(partition_louvain.values())})
print("Girvan-Newman:", {v: list(partition_gn.values()).count(v) for v in set(partition_gn.values())})
print("Label Propagation:", {v: list(partition_lp.values()).count(v) for v in set(partition_lp.values())})
