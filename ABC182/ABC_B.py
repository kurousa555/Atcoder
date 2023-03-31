import math
from sys import stdin

N = int(input())
A = list(map(int,stdin.readline().split()))

ans = None
ans_data = 0
for i in range(2,1000+1):
    tmp = 0
    for j in range(N):
        if A[j]%i == 0:tmp += 1
    if tmp > ans_data:
        ans = i
        ans_data = tmp
print(ans)
