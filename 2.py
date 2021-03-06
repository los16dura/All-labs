__author__ = 'student'
import networkx as nx
import matplotlib.pyplot as plt


G = nx.Graph()
M = int(input())
for i in range(M):
    ver1, ver2, weight = input().split()
    G.add_edge(ver1, ver2, weight = int(weight))

G1 = nx.bfs_tree(G, 'Апельсиновый')
if M > len(G1):
    print('NO')
else:
    nx.draw_circular(G1)
    plt.show()