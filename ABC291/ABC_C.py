from sys import stdin
N = int(input())
S = tuple(input())
x,y=0,0
now = (x,y)
points = set()
points.add(now)
for s in S:
    if s=="R":x+=1
    if s=="L":x-=1
    if s=="U":y+=1
    if s=="D":y-=1
    now = (x,y)
    if now in points:
        print("Yes")
        exit()
    points.add(now)
print("No")
