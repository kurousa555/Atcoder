N =int(input())
X = [int(input()) for _ in  range(N)]

ans = sum(X) - max(X)//2
print(ans)
