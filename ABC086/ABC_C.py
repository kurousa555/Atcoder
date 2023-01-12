N = int(input())
commands = tuple(tuple(map(int,input().split())) for _ in range(N))

if N==1:
    t1,x1,y1 = commands[0][0],commands[0][1],commands[0][2]
    t_diff = t1
    x_diff = abs(x1)
    y_diff = abs(y1)
    point_diff = x_diff+y_diff
    if t_diff < point_diff:
        print("No")
        exit()
    elif (t_diff > point_diff) and  ((t_diff-point_diff)%2==1):
        print("No")
        exit()
else:
    for i in range(N-1):
        t1,x1,y1 = commands[i][0],commands[i][1],commands[i][2]
        t2,x2,y2 = commands[i+1][0],commands[i+1][1],commands[i+1][2]
        t_diff = t2-t1
        x_diff = abs(x2-x1)
        y_diff = abs(y2-y1)
        point_diff = x_diff+y_diff
        if t_diff < point_diff:
            print("No")
            exit()
        elif (t_diff > point_diff) and  ((t_diff-point_diff)%2==1):
            print("No")
            exit()

print("Yes")
