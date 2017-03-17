__author__ = 'student'

n,m = [int(x) for x in input().split()]

def read_graph_as_matrix(n,m):
    graph = [[0]*n for i in range(n)]
    for j in range(m):
        a, b = [int(x) for x in input().split()]
        c = min(a, b)
        d = max(a, b)
        graph[c][d] = d
        graph[d][c] = c
    return graph

Color = [0] * (n + 1)
CycleFound = False

def DFS(start):
    Color[start] = 1
    for u in V[start]:
        if Color[u] == 0:
            DFS(u)
        elif Color[start] == 1:
          CycleFound = True
    Color[start] = 2


for i in range(1, n + 1):

    if Color[i] == 0:

        DFS(i)

print(CycleFound)
