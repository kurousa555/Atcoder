from sys import stdin
N = int(input())
A = list(map(int,stdin.readline().split()))
B = list(map(int,stdin.readline().split()))
C = list(map(int,stdin.readline().split()))
ans = sum(B)
for i in range(N-1):
    # print(A[i+1],A[i])
    if A[i+1]-A[i]==1:
        ans +=  C[A[i]-1]
print(ans)
