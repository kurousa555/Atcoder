from sys import stdin
def func():
    N = int(input())
    P = list(map(int,stdin.readline().split()))
    TrueP = sorted(P) 
    cnt = 0
    for i in range(N):
        if P[i]!=TrueP[i]:cnt+=1

    if cnt in  (0,2):
        print("YES")
    else:
        print("NO")
func()
func()
func()
