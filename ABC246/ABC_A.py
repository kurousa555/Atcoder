import collections
points = [tuple(map(int,input().split())) for _ in range(3)]
if points[0][0] == points[1][0]: x = points[2][0]
elif points[1][0] == points[2][0]: x = points[0][0]
elif points[2][0] == points[0][0]: x = points[1][0]

if points[0][1] == points[1][1]: y = points[2][1]
elif points[1][1] == points[2][1]: y = points[0][1]
elif points[2][1] == points[0][1]: y = points[1][1]

print(x,y)
