from sys import stdin
import collections
def func():
    Q = int(input())
    nums = []
    # que = collections.deque()
    idx = 0
    for _ in range(Q):
        tmp = list(map(int,stdin.readline().split()))
        if tmp[0] == 1:
            x,c = tmp[1],tmp[2]
            nums.append([x,c])
        if tmp[0] == 2:
            c = tmp[1]
            ans = 0
            while True:
                if idx >= len(nums):break
                if c ==0:break
                # print(idx,c,nums[idx][0],nums)
                if nums[idx][1] < c:
                    ans += nums[idx][0]*nums[idx][1]
                    c -= nums[idx][1]
                    nums[idx][1] = 0
                    idx += 1
                elif nums[idx][1] >= c:
                    # print(c)
                    ans += nums[idx][0]*c
                    nums[idx][1] -= c
                    c = 0
            print(ans)
    return
func()
