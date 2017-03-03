def choice_sort(C):
    for i in range(0,len(C)-1):
        for k in range(i+1,len(C)):
            if C[k] < C[i]:
                C[k],C[i] = C[i],C[k]

    return(C)

A = input().split()
B = input().split()
C = A+B
choice_sort(C)
print(' '.join(list(map(str,C))))