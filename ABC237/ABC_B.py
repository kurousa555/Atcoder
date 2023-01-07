H,W = map(int,input().split())
A = [list(map(int,input().split())) for _ in range(H)]
A = [list(x) for x in zip(*A)]
for a in A:
    print(*a)
