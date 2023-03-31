from sys import stdin
N = int(input())
X = list(map(int,stdin.readline().split()))
X.sort()

# print(X)
X = X[N:len(X)-N]
print(sum(X)/N/3)
