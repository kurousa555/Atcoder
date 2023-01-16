L,H = map(int,input().split())
N = int(input()) 
for i in range(N):
    A = int(input())
    if A<L:
        print(L-A)
    elif L<=A<=H:
        print(0)
    elif A>H:
        print(-1)
