d = input().split()
n = int(d[0])
m = int(d[1])
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])
#print(a)
b = [[0] * n for i in range(m)]
#print(b)
for i in range(0,m):
    for j in range(0,n):
        b[i][j] = a[j][i]
for k in range(0,m):
    for l in range(0,n//2):
        b[k][l],b[k][-1-l] = b[k][-1-l],b[k][l]
for row in b:
    print(' '.join([str(elem) for elem in row]))
