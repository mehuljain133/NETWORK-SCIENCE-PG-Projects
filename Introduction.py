# Unit-I Introduction: Introduction to complex systems and networks, modelling of complex systems, review of graph theory

import networkx as nx
import matplotlib.pyplot as plt
import random

# Section 1: Introduction to Complex Systems and Networks
print("=== Introduction to Complex Systems and Networks ===")
print("Complex systems consist of interconnected parts that collectively exhibit patterns.")
print("Examples: Internet, social networks, biological systems, power grids.")

# Section 2: Modeling Complex Systems with Networks
# Create different types of networks
def create_and_plot_network(G, title):
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', edge_color='gray', node_size=800)
    plt.title(title)
    plt.show()

# 1. Random Graph (Erdos-Renyi)
G_random = nx.erdos_renyi_graph(10, 0.3)
create_and_plot_network(G_random, "Random Graph (Erdos-Renyi)")

# 2. Small-World Network (Watts-Strogatz)
G_small_world = nx.watts_strogatz_graph(10, 4, 0.3)
create_and_plot_network(G_small_world, "Small-World Network (Watts-Strogatz)")

# 3. Scale-Free Network (Barabasi-Albert)
G_scale_free = nx.barabasi_albert_graph(10, 2)
create_and_plot_network(G_scale_free, "Scale-Free Network (Barabasi-Albert)")

# Section 3: Review of Graph Theory
print("\n=== Graph Theory Basics ===")
G = nx.Graph()
edges = [(1,2), (1,3), (2,4), (3,5), (5,6)]
G.add_edges_from(edges)

# Print basic properties
print("Nodes:", G.nodes())
print("Edges:", G.edges())
print("Degree of each node:", dict(G.degree()))
print("Is the graph connected?", nx.is_connected(G))
print("Shortest path from 1 to 6:", nx.shortest_path(G, source=1, target=6))

# Draw the graph
create_and_plot_network(G, "Example Graph")

# Extra: Clustering and Centrality
print("\nClustering Coefficient of each node:", nx.clustering(G))
print("Betweenness Centrality:", nx.betweenness_centrality(G))
print("Closeness Centrality:", nx.closeness_centrality(G))
