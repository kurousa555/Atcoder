N = int(input())
A = list(map(int,input().split()))


if A.count(0)>0:
    print(0)
    exit()

ans = A[0]
for i in  range(1,N):
    ans *= A[i]
    if ans > 1000000000000000000:
        print(-1)
        break
else:
    print(ans)
