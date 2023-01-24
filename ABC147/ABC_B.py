S =  input()
lenS = len(S)
ans = 0
for i in range(lenS//2):

    if S[i]!=S[-1-i]:ans+=1
print(ans)
