from sys import stdin
def func():
    N = int(input())
    A = list(map(int,stdin.readline().split()))
    A.sort()
    ans = 0
    for i in range(N-1):
        ans += abs(A[i+1]-A[i])
    print(ans)
func()
# func()
