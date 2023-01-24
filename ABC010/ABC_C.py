initx,inity,tarx,tary,T,V = map(int,input().split())
n = int(input())
dis = 0
judge = False
import math

for i  in range(n):
    x,y = map(int,input().split())
    dis += math.sqrt((x-initx)**2 + (y-inity)**2)
    dis += math.sqrt((x-tarx)**2 + (y-tary)**2)
    # print(dis)
    if dis <= T*V:
        print("YES")
        exit()
    dis = 0
else:
    print("NO")
