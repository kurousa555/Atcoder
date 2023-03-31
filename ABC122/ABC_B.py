S = input()
ans = 0
tmp =  0
for i in range(len(S)):
    if S[i] in ("A","C","G","T"):
        tmp += 1
        ans = max(ans,tmp)
    else:
        tmp = 0
print(ans)
