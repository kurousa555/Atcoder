from sys import stdin
def func():
    N,K = map(int,stdin.readline().split())
    P = list(map(int,stdin.readline().split()))
    P = [(p*(p+1)/2)/p for p in P]
    init = sum(P[:K])
    ans = [init]
    # print(P)
    for i in range(K,N):
        init += P[i]
        init -= P[i-K]
        ans.append(init)
    print(max(ans))
    return
func()
