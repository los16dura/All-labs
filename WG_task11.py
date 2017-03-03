n, m = [int(x) for x in input().split()]

def reading(n, m):
    graph = [[0]*n for i in range(n)]
    for j in range(m):
        a, b = [int(x) for x in input().split()]
        c = min(a, b)
        d = max(a, b)
        graph[c][d] = d
        graph[d][c] = c
    return graph

def bfs(G, start, used = None):
    path = {start: 0}
    if used is None:
        used = set()
    used.add(start)
    Q = [start]
    while Q:
        t = Q.pop(0)
        for c in G[t]:
            if c not in used:
                used.add(c)
                Q.append(c)
                path[c] = path[t] + 1
                print(t, c)

A = reading(n, m)
bfs(A, 1)