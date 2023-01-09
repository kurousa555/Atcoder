x,y = map(int,input().split())
if x == y:
    print(x)
if x != y:
    if x==0 and y ==1:print(2)
    if x==1 and y ==2:print(0)
    if x==2 and y ==0:print(1)
    if y==0 and x ==1:print(2)
    if y==1 and x ==2:print(0)
    if y==2 and x ==0:print(1)
