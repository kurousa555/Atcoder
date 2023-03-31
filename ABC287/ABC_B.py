def judge():
    from sys import stdin
    N,M = map(int,stdin.readline().split())
    S = list()
    T = set()
    for _ in range(N):
        S.append(input()[-3:])
        

    for _ in range(M):
        T.add(input())

    ans = 0
    for s  in S:
        if s in T:ans += 1
    print(ans)

judge()
