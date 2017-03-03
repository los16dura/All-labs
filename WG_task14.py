def reading(n, m):
    mass = []
    for i in range(n):
        st = input()
        for j in range(m):
            if st[j] == ' ':
                mass.append([i, j])
    return mass

def read(n, m, x, spisok):
    graph = [[x]*n for i in range(n)]
    for j in range(m):
        c, d = [int(x) for x in spisok[j].split()]
        a = min(c, d)
        b = max(c, d)
        graph[a][b] = b
        graph[b][a] = a
    return graph

def bfs(G, start, finish, fired = None):
    time = {start: 0}
    if fired is None:
        fired = set()
    fired.add(start)
    Q = [start]
    while Q:
        c = Q.pop(0)
        for n in G[c]:
            if n not in fired:
                fired.add(n)
                Q.append(n)
                time[n] = time[c] + 1
    if finish in time:
        print(time[finish])
    else:
        print('INF')

n, m = map(int, input().split())
x = list(map(int, input().split()))
y = list(map(int, input().split()))
A = reading(n, m)
if x not in A or y not in A:
    print('INF')
else:
    x = A.index(x)
    y = A.index(y)
    spisok = []
    for i in A:
        for di, dj in [(-1, 0), (1,0), (0, -1), (0, 1)]:
            ni = i[0] + di
            nj = i[1] + dj
            if [ni, nj] in A:
                spisok.append(' '.join([str(A.index(i)), str(A.index([ni, nj]))]))
    G = read(len(A), len(spisok), x, spisok)
    bfs(G, x, y)