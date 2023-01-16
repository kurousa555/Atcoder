import  collections
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
newB = [None]*N
for i in range(N):
    newB[i] = B[C[i]-1]

A = collections.Counter(A)
B = collections.Counter(newB)
ans = 0
for i in range(1,N+1):
    ans += A[i]*B[i]

print(ans)
