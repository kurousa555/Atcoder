N,M,C = map(int,input().split())
B = tuple(map(int,input().split()))
ans = 0
for _ in range(N):
    A = tuple(map(int,input().split()))
    cnt = 0
    for i in range(M):
        cnt += A[i]*B[i]
    if cnt+C >0:ans += 1
print(ans)
