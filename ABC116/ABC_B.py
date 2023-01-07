s = int(input())
nums = set([s])

for i in range(1,10**6):
    num = list(nums)[-1]
    if num%2 == 0:
        new_num = num//2 
    elif num%2 == 1:
        new_num = 3*num+1

    if new_num in nums:
        print(i+1)
        break
    nums.add(new_num)



# print(nums)
