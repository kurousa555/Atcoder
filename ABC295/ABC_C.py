from sys import stdin
import collections
def func():
    N = int(input())
    A = list(map(int,stdin.readline().split()))
    A  = collections.Counter(A)
    ans = 0
    for a in A:
        # print(a)
        # print(A[a])
        ans +=  A[a]//2
    # print(A)
    print(ans)
func()
