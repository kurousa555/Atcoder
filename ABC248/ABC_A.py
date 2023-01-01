S = list(input())
nums = [i for i in range(0,10)]
for s in S:
    nums.remove(int(s))
print(*nums)
