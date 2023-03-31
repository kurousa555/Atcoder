from sys import stdin
import math
N = int(input())
X = list(map(int,stdin.readline().split()))
man=0
che=0
euq=0
for x in X:
    man += abs(x)
    che += x**2
    euq = max(euq,abs(x))

print(man)
print(math.sqrt(che))
print(euq)
