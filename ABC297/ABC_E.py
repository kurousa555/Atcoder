n, k = map(int, input().split())
a = list(map(int, input().split()))

INF = float('inf')
dp = [INF] * (k+1)
dp[0] = 0

for i in range(n):
    for j in range(k+1):
        if j >= a[i]:
            dp[j] = min(dp[j], dp[j-a[i]] + a[i])

if dp[k] == INF:
    print(-1)
else:
    print(dp[k])
