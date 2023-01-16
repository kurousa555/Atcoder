N,Q = map(int,input().split())
A = [0]*N

for _ in range(Q):
    L,R,T=map(int,input().split())
    L-=1
    A[L:R] = [T]*(R-L)
    # print(A)

for a in A:
    print(a)
