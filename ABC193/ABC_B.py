N = int(input()) 
ans = 1000000000000000000
for _ in range(N):
    a,p,x = map(int,input().split())
    if x-a>0:
        ans = min(ans,p)
if ans == 1000000000000000000:ans=-1
print(ans)
