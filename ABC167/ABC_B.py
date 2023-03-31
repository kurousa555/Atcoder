A,B,C,K = map(int,input().split())
ans = 0
ans += min(A,K)
K =  max(0,K-A)
K = max(0,K-B)
ans -= min(C,K)
print(ans)

