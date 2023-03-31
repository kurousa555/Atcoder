from sys import stdin
def func():
    N,M = map(int,stdin.readline().split())
    A = list(map(int,stdin.readline().split()))
    B = list(map(int,stdin.readline().split()))
    ans = 0
    for b in B:
        ans += A[b-1]
    print(ans)

func()
