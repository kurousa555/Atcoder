from sys import stdin
import itertools
def func():
    nums = list(map(int,stdin.readline().split()))
    sums = list(map(sum,list(itertools.combinations(nums,3))))
    sums.sort()
    print(sums[-3])
    return
func()
