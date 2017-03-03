n, m = map(int, input().split())
A = list(map(int, input().split()))

for i in range(n):
    print(' '.join(map(str, A[m*i:m*(i+1)])))