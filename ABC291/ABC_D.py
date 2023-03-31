from sys import stdin
N = int(input())


DP1 = [1]+[0]*(N-1)
DP2 = [1]+[0]*(N-1)
A = []
B = []
mod = 998244353
for _ in range(N):
    a,b = map(int,stdin.readline().split())
    A.append(a)
    B.append(b)

for i in range(N):

    if DP1[i-1] == 0 and DP2[i-1] == 0:
        break

    if A[i] != A[i-1]:DP1[i] += DP1[i-1]
    if A[i] != B[i-1]:DP1[i] += DP2[i-1]
    if B[i] != A[i-1]:DP2[i] += DP1[i-1]
    if B[i] != B[i-1]:DP2[i] += DP2[i-1]
    DP1[i] %= mod
    DP2[i] %= mod
# print(DP1)
# print(DP2)
# print(A)
# print(B)
print((DP1[-1]+DP2[-1]) % 998244353)
