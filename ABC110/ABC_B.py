from sys import stdin
def func():
    N,M,X,Y = map(int,stdin.readline().split())
    x = list(map(int,stdin.readline().split()))
    y = list(map(int,stdin.readline().split()))
    max_x = max(x) 
    min_y = min(y)
    for z in range(X+1,Y+1):
        if z > max_x and z <= min_y:
            print("No War")
            exit()
    print("War")

func()
