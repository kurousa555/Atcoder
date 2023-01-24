def func():
    N,P,Q,R,S = map(int,input().split())
    A = list(map(int,input().split()))
    # print(A)
    A[P-1:Q],A[R-1:S] =A[R-1:S],A[P-1:Q]
    print(*A)
func()
# 5 6 7 4 1 2 3 8
