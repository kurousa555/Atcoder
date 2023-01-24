import collections,math
N = int(input())
S = [list(input()) for _ in range(N)]
for i in range(N):
    S[i].sort()
    S[i] = "".join(S[i])
S = collections.Counter(S)
ans  = 0
# print(S)
for s in S:
    # print(S[s])
    if S[s]>=2:
        ans  += math.factorial(S[s])//math.factorial(2)//math.factorial(S[s]-2)
    
print(ans)
