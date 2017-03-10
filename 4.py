__author__ = 'student'
import networkx as nx
import matplotlib.pyplot as plt
c = ['r','g','b']

G = nx.Graph()
M = int(input())
for i in range(M):
    ver1, ver2, weight = input().split()
    G.add_edge(ver1, ver2, weight = int(weight))

graphs = list(nx.connected_component_subgraphs(G))
#nx.draw_circular(G)
for i in range(len(graphs)):
    nx.draw(graphs[i],node_color = c[i])

plt.show()
