from sys import stdin
def func():
    N,D = map(int,stdin.readline().split())
    T  = list(map(int,stdin.readline().split()))
    for i in range(N-1):
        # print(T[i],T[i+1])
        if T[i+1]-T[i] <= D:
            print(T[i+1])
            exit()
    print(-1)
    return
func()
