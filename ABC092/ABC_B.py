from sys import stdin
import math
def judge():
    N = int(input())
    D,X = map(int,stdin.readline().split())
    for _ in range(N):
        A = int(input())
        X +=  math.ceil(D/A)
    print(X)

judge()
# judge()
# judge()
