def func():
    import math
    A,B,C,D = map(int,input().split())
    if C*D-B==0:
        print(-1)
        exit()
        
    tmp =A/(C*D-B)

    if tmp<0:
        print(-1)
    else:
        print(math.ceil(A/(C*D-B)))
func()
