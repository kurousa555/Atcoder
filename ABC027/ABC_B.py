from sys import stdin
def func():
    N  = int(input())
    A = list(map(int,stdin.readline().split()))
    bridge  = [False]*(N-1)

    if len(set(A)) == 1:
        print(0)
        exit()
    if sum(A)%N!=0:
        print(-1)
        return
    # print(A)
    num = sum(A)//N
    for i in range(N-1):
        if A[i]>num:
            A[i+1] += A[i]-num
            A[i] =  num
            bridge[i] =  True
    A = list(reversed(A))
    bridge = list(reversed(bridge))
    for i in range(N-1):
        if A[i]>num:
            A[i+1] += A[i]-num
            A[i] =  num
            bridge[i] =  True

    print(bridge.count(True))

func()
# func()
# func()
# func()
