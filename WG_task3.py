def bfs_fire(graph,start,end,fired=None):
    time = {start:0}
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
                time[neighbour] = time[current]+1
    if end in time:
        print(time[end])
        #print(neighbour)


def read_graph_as_lists(n, m):
    graph = [[] for i in range(n)]
    for edge in range(m):
        a,b = [int(x) for x in input().split()]
        graph[a].append(b)
        graph[b].append(a)
    return graph

n, m, x, y = [int(j) for j in input().split()]
A = read_graph_as_lists(n,m)
#print(A)
bfs_fire(A,x,y)