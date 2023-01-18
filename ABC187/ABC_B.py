N = int(input())
points = [list(map(int,input().split())) for _ in range(N)]
ans = 0 
for  i in range(N):
    for j in range(i+1,N):
        x1,y1 = points[i][0],points[i][1]
        x2,y2 = points[j][0],points[j][1]
        if abs(points[i][1] - points[j][1]) <= abs(points[i][0] - points[j][0]):ans+=1
print(ans)
