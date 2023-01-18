import collections
N,K = map(int,input().split())
A = list(map(int,input().split()))
A = collections.Counter(A)
A = sorted(A.items(), reverse=True,key=lambda x:x[1])
A = A[K:]
ans = 0
for a in A:
    ans += a[1]

print(ans)
