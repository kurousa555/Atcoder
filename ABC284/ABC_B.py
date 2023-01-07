N = int(input())
for _ in range(N):
    test = int(input())
    nums = tuple(map(int,input().split()))
    cnt = 0
    for num in nums:
        if num%2 != 0:cnt+=1
    print(cnt)
