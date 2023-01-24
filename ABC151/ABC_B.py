N,M,K = map(int,input().split())
A = list(map(int,input().split()))
ans = max(0,N*K - sum(A))
# print(ans)
if 0<=ans<=M:
    print(ans)
else:
    print(-1)
