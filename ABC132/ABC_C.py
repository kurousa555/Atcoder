from sys import stdin
N = int(input())
D = list(map(int,stdin.readline().split()))
D.sort()
# print(D)
# print(D[N//2],D[N//2-1])
print(D[N//2]-D[N//2-1])
