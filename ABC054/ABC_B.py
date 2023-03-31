from sys import stdin
def func():
    N,M = map(int,stdin.readline().split())
    A = [list(input()) for _  in range(N)]
    B = [list(input()) for _  in range(M)]
    # print(A)
    for y in range(N-M+1):
        # print(A[y:y+M],y,y+M-1, x,x+M-1)
        pre_target = A[y:y+M]
        for x in range(N-M+1):    
            # print(pre_target,x,x+M-1)
            target = [pre_target[x:x+M] for pre_target in pre_target]
            # print(target)
            if target == B:
                print("Yes")
                exit()
    print("No")
func()
