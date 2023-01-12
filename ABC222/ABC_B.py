N,P = map(int,input().split())
nums = list(map(int,input().split()))
new_nums = [num for num in nums if num<P]
print(len(new_nums))
