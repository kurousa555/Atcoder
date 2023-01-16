N = int(input())
# N = 10**9

ans = 0
cnt = 0
for i in range(1,N+1):
    ans +=  i
    cnt += 1
    if ans >= N:
        print(cnt)
        break
