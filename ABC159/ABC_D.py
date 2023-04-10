from sys import stdin
import collections
import math
def func():
    N = int(input())
    A = list(map(int,stdin.readline().split()))
    cntA = collections.Counter(A)
    total = 0
    # print(cntA)
    for a in cntA:
        # if cntA[a]>=2:total += int(math.factorial(cntA[a])/math.factorial(cntA[a]-2)/math.factorial(2))
        total += cntA[a]*(cntA[a]-1)//2
        # print(cntA[a],cntA[a]-1)
    for a in A:
        if  cntA[a]>=2:
            # minus = int(math.factorial(cntA[a])/math.factorial(cntA[a]-2)/math.factorial(2))
            minus = cntA[a]*(cntA[a]-1)//2
        else:
            minus = 0

        if  cntA[a]>=3:
            # plus = int(math.factorial(cntA[a]-1)/math.factorial(cntA[a]-2-1)/math.factorial(2))
            plus = (cntA[a]-1)*(cntA[a]-2)//2
        else:
            plus = 0

        # print(total,minus,plus)
        ans = total - minus + plus
        print(ans)
    return
func()
