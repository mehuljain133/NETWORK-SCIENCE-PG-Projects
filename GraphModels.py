# Unit-III Graph models: Random graph model, Small world network model, Barabasi-Albert (preferential attachment) network model.

import networkx as nx
import matplotlib.pyplot as plt

def draw_network(G, title):
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=800)
    plt.title(title)
    plt.show()

# 1. Random Graph Model (Erdős–Rényi)
print("=== Random Graph Model ===")
n, p = 10, 0.3  # nodes, probability of edge
G_random = nx.erdos_renyi_graph(n, p)
draw_network(G_random, "Random Graph (Erdős–Rényi Model)")
print("Number of nodes:", G_random.number_of_nodes())
print("Number of edges:", G_random.number_of_edges())

# 2. Small-World Network Model (Watts-Strogatz)
print("\n=== Small-World Network Model ===")
n, k, p = 10, 4, 0.2  # nodes, each node connected to k nearest neighbors in ring topology, rewiring prob.
G_small_world = nx.watts_strogatz_graph(n, k, p)
draw_network(G_small_world, "Small-World Network (Watts-Strogatz Model)")
print("Clustering coefficient:", nx.average_clustering(G_small_world))
print("Average shortest path length:", nx.average_shortest_path_length(G_small_world))

# 3. Barabási–Albert Model (Preferential Attachment)
print("\n=== Barabási–Albert Model ===")
n, m = 10, 2  # nodes, edges to attach from new node to existing nodes
G_ba = nx.barabasi_albert_graph(n, m)
draw_network(G_ba, "Barabási–Albert Network (Preferential Attachment)")
print("Degree distribution:", dict(G_ba.degree()))
print("Number of edges:", G_ba.number_of_edges())
