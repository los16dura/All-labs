__author__ = 'student'
import networkx as nx
import matplotlib.pyplot as plt
c = ['r','g','b']

G = nx.Graph()
M = int(input())
for i in range(M):
    ver1, ver2, weight = input().split()
    G.add_edge(ver1, ver2, weight = int(weight))
dlina = []
for i in len(G.nodes):
    dlina.add(nx.Bidirectional_dijkstra(G, i))
nx.draw(graphs[i],node_color = c[i])
