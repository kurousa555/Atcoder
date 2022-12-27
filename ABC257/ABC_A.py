import string
N, X = map(int,input().split())
alpha = []
for i in range(ord("A"),ord("Z")+1):
    for j in range(N):
        alpha.append(chr(i))
print(alpha[X-1])
