from sys import stdin
N,M = map(int,stdin.readline().split())
A = list(map(int,stdin.readline().split()))
print(max(-1,N-sum(A)))
