from sys import stdin
def func():
    A,B = map(int,stdin.readline().split())
    ans = 0
    while A!=B:
        if A>B:
            # print(A,B)
            mod = A//B
            if A%B==0:mod-=1
            A = A-B*mod
            ans += mod
        elif A<B:
            mod = B//A
            if B%A==0:mod-=1
            B = B-A*mod
            ans +=  mod
        if A==B:break 
        # print(A,B)

    print(ans)
    return
func()
