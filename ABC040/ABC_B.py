from sys import stdin
import math
minimum = []
def func():
    n =  int(input())
    if n == 1:
        print(0)
        exit()
    for x in range(1,n//2+1):
        # y = n - x
        y  = int(n / x)
        leaves = n - x*y
        minimum.append(abs(x-y)+leaves)
        # print(x,y,leaves)
    print(min(minimum))
    return
func()
