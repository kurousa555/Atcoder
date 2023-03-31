from sys import stdin
def func():
    N,K = map(int,stdin.readline().split())
    L = list(map(int,stdin.readline().split()))
    L.sort()
    ans = sum(L[-K:])
    print(ans)

func()
# func()

