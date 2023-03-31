from sys import stdin
N = int(input())
V = list(map(int,stdin.readline().split()))
V.sort()
for i in range(1,N):
    V[i] = (V[i]+V[i-1])/2
print(V[-1])

