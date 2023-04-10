from sys import stdin
def func():
    # N,X  = map(int,stdin.readline().split())
    N, X = map(int, input().split())
    dp = [[False]*(X+1) for _ in range(N+1)]
    dp[0][0] = True
    for i in range(N):
        a,b  = map(int,stdin.readline().split())
        for j in range(X+1):
            if dp[i][j] == True:
                if j + a <= X:
                    dp[i + 1][j + a] = True
                if j + b <= X:
                    dp[i + 1][j + b] = True
    return dp[N][X]
print('Yes' if func() else 'No')

