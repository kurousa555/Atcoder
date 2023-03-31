from sys import stdin
import math

def func():
    R,X,Y = map(int,stdin.readline().split())
    dis = math.sqrt(X**2 +  Y**2)
    print(dis)
    if  dis%R==0:
        print(int(dis//R))
    else:
        print(math.ceil(dis/R))
func()
# func()
# func()
