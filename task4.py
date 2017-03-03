n = int(input())
A = list(map(int, input().split()))
A = sorted(A)
r = 0
for i in range(len(A)//2,len(A)):
    r+=A[i]
print(r)