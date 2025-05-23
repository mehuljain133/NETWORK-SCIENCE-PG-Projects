# Unit-II Network properties: Local and global properties like clustering coefficient, eccentricity; centrality measures for directed and undirected networks.

import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(G, title):
    pos = nx.spring_layout(G, seed=42)
    plt.figure(figsize=(6, 4))
    nx.draw(G, pos, with_labels=True, node_color='lightgreen', edge_color='gray', node_size=800)
    plt.title(title)
    plt.show()

# Section 1: Undirected Network
print("=== Undirected Network ===")
G_undirected = nx.Graph()
G_undirected.add_edges_from([
    (1, 2), (1, 3), (2, 4), (3, 4), (3, 5), (5, 6), (6, 7), (5, 7)
])

draw_graph(G_undirected, "Undirected Graph")

# Local Properties
print("\nClustering Coefficient (Local):", nx.clustering(G_undirected))
print("Eccentricity (Global):", nx.eccentricity(G_undirected))

# Centrality Measures (Undirected)
print("\nDegree Centrality:", nx.degree_centrality(G_undirected))
print("Betweenness Centrality:", nx.betweenness_centrality(G_undirected))
print("Closeness Centrality:", nx.closeness_centrality(G_undirected))
print("Eigenvector Centrality:", nx.eigenvector_centrality(G_undirected))

# Section 2: Directed Network
print("\n=== Directed Network ===")
G_directed = nx.DiGraph()
G_directed.add_edges_from([
    (1, 2), (2, 3), (2, 4), (3, 5), (5, 6), (6, 2)
])

draw_graph(G_directed, "Directed Graph")

# Local Properties (Clustering for directed graphs)
print("\nClustering Coefficient (Local, Directed):", nx.clustering(G_directed.to_undirected()))
print("Eccentricity (Directed):", nx.eccentricity(G_directed.to_undirected()))

# Centrality Measures (Directed)
print("\nIn-Degree Centrality:", G_directed.in_degree())
print("Out-Degree Centrality:", G_directed.out_degree())
print("Betweenness Centrality:", nx.betweenness_centrality(G_directed))
print("Closeness Centrality:", nx.closeness_centrality(G_directed))
print("Eigenvector Centrality:", nx.eigenvector_centrality(G_directed.to_undirected()))
