A = set('0123456789')
B = set('02468')
C = set('12345')
D = set('56789')
M = A-B
N = C-D
K = D - A
L = B - C
M &= N
K &= L
M |= K
print(M)
