N,X = map(int,input().split())
L = list(map(int,input().split()))
ans = 1
now = 0
for l  in L:
    now += l
    if  now<=X:
        ans+=1
print(ans)
