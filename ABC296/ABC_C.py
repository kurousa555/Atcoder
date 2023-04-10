from sys import stdin
import collections
def func():
    N,X = map(int,stdin.readline().split())
    A = list(map(int,stdin.readline().split()))
    # nums = collections.Counter(A)
    nums = set(A)
    for i in range(N):
        tar = X + A[i]
        # print(tar)
        if tar in nums:
            # print(A[i], X+A[i])
            print("Yes")
            exit()
    print("No")
    return
func()
