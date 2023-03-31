n,X = map(int,input().split())
A = list(map(int,input().split()))
ans = 0
for shift in range(len(A)):
    if int(X)>>shift & 1 == 1:
        ans += A[shift]
print(ans)

