N  = int(input())
S = list(input())
ans = 0
for i in range(1,N):
    S1 = set(S[0:i])
    S2 = set(S[i:])
    tmp=0
    for s in S1:
        if s in S2:tmp+=1
    if tmp>ans:ans=tmp
    # print(S1,S2,ans)
    # print(S[0:i],S[i:])
    # print("="*40)

print(ans)
