N,K = map(int,input().split())
C = tuple(input().split())
maximum = 0
for i in range(N-K+1):
    if  len(set(C[i:i+K])) > maximum:
        maximum = len(set(C[i:i+K]))
print(maximum)

