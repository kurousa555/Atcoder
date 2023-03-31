from sys import stdin
import math
import collections
N = int(input())
A = list(map(int,stdin.readline().split()))
A =  collections.Counter(A)
# print(A)
ans = math.factorial(N)//math.factorial(N-2)//math.factorial(2)
# print(ans)
for a in A.items():
    if a[1]>=2:
        ans -= math.factorial(a[1])//math.factorial(a[1]-2)//math.factorial(2)

print(ans)
