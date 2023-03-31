from sys import stdin
N,Q = map(int,stdin.readline().split())
player = [2 for _ in range(N+1)]
for _ in range(Q):
    c,x = map(int,stdin.readline().split())
    if c==1:player[x]-=1
    if c==2:player[x]=0
    if c==3:
        if player[x]<=0:print("Yes")
        else:print("No")
