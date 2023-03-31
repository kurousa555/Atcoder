from sys import stdin
N = int(input())
A = list(map(int,stdin.readline().split()))
A.sort()
total = sum(A)
ans = 0

for i in range(N):
    total -= A[i]
    ans += total
    ans -= A[i]*(N-i-1)
print(ans)

#絶対値の差の総和を求める場合はsortしてしまってよい。


