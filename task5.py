A = input().split()
B = input().split()
m = int(A[0])
n = int(A[1])
C = [[0] * n for i in range(m)]
#print(C)
for i in range(0,m):
    for j in range(0,n):
        C[i][j] = B[j+i*n]
for row in C:
    print(' '.join([str(elem) for elem in row]))
