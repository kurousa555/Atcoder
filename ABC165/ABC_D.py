from sys import stdin
A,B,N = map(int,stdin.readline().split())
A
import math
print(A,B,N)
for x in range(int(math.sqrt(N))):
    first  = math.floor(A*x/B)
    second = A*math.floor(x/B)
    print(first,second,x)
