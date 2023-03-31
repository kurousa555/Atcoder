N = int(input())
H =  list(map(int,input().split()))
maxi = H[0]
ans = 1
for i in range(1,N):
    if H[i]>=maxi:
        ans+=1
        maxi = max(maxi,H[i])
print(ans)
