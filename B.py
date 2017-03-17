__author__ = 'los'
import sys


def read_graph_as_lists(n, m):
    graph = [[] for i in range(n)]
    for edge in range(m):
        a,b = [int(x) for x in input().split()]
        graph[a].append(b)

    return graph


N, M = [int(x) for x in input().split()]
Visited = [False] * (N)
Ans = []
G = read_graph_as_lists(N, M)
#print(G)

def DFS(start):
    Visited[start] = True
    for u in G[start]:
        if not Visited[u]:
            DFS(u)
    Ans.append(start)



for i in range(N):
    if not Visited[i]:
        DFS(i)
Ans = Ans[::-1]
print(*Ans)


