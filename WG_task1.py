def bfs_fire(graph,start,fired=None):
    path = {start: 0}
    if fired is None:
        fired = set()
    fired.add(start)
    Q = [start]
    while Q: #пока список не пуст
        current = Q.pop(0)
        for neighbour in graph[current]:
            if neighbour not in fired:
                fired.add(neighbour)
                Q.append(neighbour)
                path[neighbour] = path[current]+1
    for i in range(0,m+1):
        if i in path:
            print(path[i])
            #print(neighbour)


def read_graph_as_matrix(n, m):
    graph = [[0]*n for i in range(n)]
    for j in range(m):
        a, b = [int(x) for x in input().split()]
        c = min(a, b)
        d = max(a, b)
        graph[c][d] = d
        graph[d][c] = c
    return graph

n, m = [int(x) for x in input().split()]
A = read_graph_as_matrix(n,m)
#print(A)
bfs_fire(A,0)
