from sys import stdin
def func():
    N  = int(input())
    W = list(map(int,stdin.readline().split()))
    ans = 100000000
    for t in range(1,N):
        S1 = W[:t]
        S2 = W[t:]
        ans = min(ans,abs(sum(S1)-sum(S2)))
        # print(S1,S2)
    print(ans)
func()
# func()
# func()
