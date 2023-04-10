from sys import stdin
def func():
    H,W,N = map(int,stdin.readline().split())
    A,B = [],[]
    for _ in range(N):
        a,b = map(int,stdin.readline().split())
        A.append(a)
        B.append(b)
    Rs = sorted(set(A)) 
    Cs = sorted(set(B))
    # print(Rs,Cs)
    Rd = {x: i for i, x in enumerate(Rs, 1)}
    Cd = {x: i for i, x in enumerate(Cs, 1)}
    # print(Rd,Cd)
    for r, c in zip(A, B):
        print(Rd[r], Cd[c])
func()
