from itertools import product
import math
N,X = map(int,input().split())
A =  []
for i in range(N):
    l,*a = map(int,input().split())
    A.append(a)

A = [*map(list, product(*A))]
A = list(map(math.prod, A))

print(A.count(X))

