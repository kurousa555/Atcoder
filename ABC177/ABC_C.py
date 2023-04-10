from sys import stdin
def func():
    N = int(input())
    A =  list(map(int,stdin.readline().split()))
    ans = 0
    total = sum(A)
    mod = 1000000007
    for i in range(N):
        total -= A[i]
        first = A[i]
        ans += (total * first)
    print(ans%mod)
    return
func()

