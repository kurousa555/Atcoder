X,N = map(int,input().split())
P = list(map(int,input().split()))
ans = X
ans_abs = float("inf")

# print(P)
for num in range(0,102):
    if num in P:continue
    tmp = abs(num-X)
    # print(num,X,tmp,ans)
    if tmp  < ans_abs:
        ans=num
        ans_abs=tmp
print(ans)
