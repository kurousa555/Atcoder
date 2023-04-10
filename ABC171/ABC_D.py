from sys import stdin
import collections
def func():
    N = int(input())
    A = list(map(int,stdin.readline().split()))
    total = sum(A)
    Q = int(input())
    cntA = collections.Counter(A)
    # print(total)
    for _  in range(Q):
        B,C = map(int,stdin.readline().split())
        total  += (C-B)*cntA[B]
        cntA[C] += cntA[B]
        cntA[B]=0
        
        print(total)
    # print(cntA)
    return
func()
