N = int(input())
nums = tuple(map(int,input().split()))

maximum=-1
for i in range(N):
    if (nums[i]-1) > maximum:
        maximum=(nums[i]-1)
    if nums[i] < maximum:
        print("No")
        exit()
        
print("Yes")
