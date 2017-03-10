__author__ = 'student'
import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
M = int(input())
for i in range(M):
    ver1, ver2 , weight = input().split()
    G.add_edge(ver1, ver2, weight = int(weight))

nx.draw_circular(G)
plt.show()
