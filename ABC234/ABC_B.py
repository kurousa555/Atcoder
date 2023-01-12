import math
N = int(input())
points = [tuple(map(int,input().split())) for _ in range(N)]
diffs = []
for i in range(N):
    for j in range(i+1,N):
        diff = math.sqrt((points[i][0]-points[j][0])**2 + (points[i][1]-points[j][1])**2)
        diffs.append(diff)

print(max(diffs))
