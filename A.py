import sys


def read_graph_as_matrix(n, m):
    graph = [[None]*n for i in range(n)]
    for j in range(1, m+1):
        a, b = map(int, input().split())
        graph[a][b] = b
    return graph


def dfs(start,friends,nodes = None, stack = None):
    if nodes is None:
        nodes = set()
    if stack is None:
        stack = []
    nodes.add(start)
    stack.append(start)
    for friend in friends[start]:
        if friend == None:
            continue
        if friend not in nodes:
            dfs(friend,friends,nodes,stack)
        elif friend == stack[0]:
            print(*stack)
            sys.exit()
    stack.pop(-1)

N, M = [int(x) for x in input().split()]
A = read_graph_as_matrix(N, M)
for i in range(N):
    dfs(i, A)
print('YES')