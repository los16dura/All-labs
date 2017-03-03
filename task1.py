n = int(input())
B = {}

for i in range(n):
    A = input().split()
    B[A[0]] = A[1]
C = {}
for k in range(n):
    A = input().split()
    C[A[0]] = A[1]
for key in C:
    print(B[key], C[key])