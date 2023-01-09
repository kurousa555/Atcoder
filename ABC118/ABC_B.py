N,M = map(int,input().split())
minor   = -1000000
maximum =  1000000
nums = []
for i in range(N):
    get = list(map(int,input().split()))
    A = sorted(get[1:])
    A = [a for a in A if minor<=a<=maximum]
    if len(A)==0:
        print(0)
        exit()

    if A[0] > minor:minor=A[0]
    if A[-1] < maximum:maximum=A[-1]  
    nums.append(A)

len_list = []
for i in range(N):
    nums[i] = [a for a in nums[i] if minor<=a<=maximum]
    len_list.append(len(nums[i]))

print(min(len_list))

