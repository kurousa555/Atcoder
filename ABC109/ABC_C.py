from sys import stdin
import math

N,X = map(int,stdin.readline().split())
x = list(map(int,stdin.readline().split()))
x.append(X)
x.sort()
dis = [0]*N

for i in range(N):
    dis[i]=abs(x[i]-x[i+1])

def gcd_l(list_g2):
   for i in reversed(range(1, min(list_g2)+1)):
      if any([j % i for j in list_g2]) == False:
         return i
print(gcd_l(dis))
