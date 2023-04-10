from sys import stdin
def func():
    N = int(input())
    nums  = set()
    for _ in range(N):
        a = int(input())
        if a in nums:nums.remove(a)
        elif a not in nums:nums.add(a)
    return len(nums)
print(func())
