import math
N,K = map(int,input().split())
A = list(map(int,input().split()))
x_y  = [tuple(map(int,input().split())) for _ in range(N)]

min_dis = []
for i in range(N):
    distances = []
    for a in A:
        if (i+1) not in A:
            distance = math.sqrt((x_y[i][0]-x_y[a-1][0])**2 + (x_y[i][1]-x_y[a-1][1])**2)   
            distances.append(distance)

    if len(distances) != 0:
        # print(min(distances))
        min_dis.append(min(distances))
print(max(min_dis))
