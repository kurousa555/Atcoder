S = list(input())
length = len(S)
for i in range(0,length,2):
    S[i],S[i+1] = S[i+1],S[i]
print("".join(S))
