S = list(input())
a,b = map(int,input().split())
prea  = S[a-1]
S[a-1] = S[b-1]
S[b-1] = prea
print("".join(S))

