def read_graph_as_lists(n,m):
    graph = [[] for i in range(n)]
    for edge in range(m):
        a,b = [int(x) for x in input().split()]
        graph[a].append(b)
        #graph[b].append(a)
    return graph

n, m = [int(x) for x in input().split()]
A = read_graph_as_lists(n, m)


def bfs_fire(graph, start, fired=None):
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
            elif neighbour == start:
                break
                break
    for i in range(0, m+1):
        if i in path:
            print(path[i])
            #print(neighbour)
bfs_fire(A,0)


# def dfs(start):
#     color[start] = 1
#     for u in range(len(g[start])):
#         if(color[g[start[u]]] == 0):
#             dfs(g[start][u])
#         elif(color[g[start][u]]) == 1:
#             cycle = true;
#         color[start] = 2
# cycle = false;
# for i in range(n):
#     if(color[i] == 0):
#         dfs(i)