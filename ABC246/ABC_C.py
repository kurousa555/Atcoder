N, K, X = map(int,input().split())
A = list(map(int,input().split()))
A = sorted(A,reverse=True)

for i in range(N):
    if K==0:break
    minor = min(A[i]//X, K)
    A[i] -= minor*X
    K -= minor

A = sorted(A,reverse=True)
A[0:K] = [0] 
print(sum(A))
