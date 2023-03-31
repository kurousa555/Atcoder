from sys import stdin
import itertools
def func():
    N,K = map(int,stdin.readline().split())
    ans =  0
    orders = list(itertools.permutations(range(2,N+1),N-1))
    T = [list(map(int,stdin.readline().split())) for _ in range(N)]
    for i in range(len(orders)):
        tmp = 0
        now=1
        for order in orders[i]:
            # print(now,order)
            tmp += T[now-1][order-1]
            # print(T[now-1][order-1])
            now = order
        tmp += T[now-1][1-1]
        if tmp==K:ans+=1
    print(ans)
func()
