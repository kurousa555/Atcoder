N = int(input())
S = list(input())
# Es = S.count("E")
# Ws = S.count("W")
ans = S[1:].count("E")
tmp = S[1:].count("E")
for i in range(1,N):
    # print(tmp,S[i-1],S[i])
    if S[i-1]=="W" and S[i]=="E":
        tmp += 1
        tmp -= 1
        if tmp<ans:ans=tmp

    elif S[i-1]=="W" and S[i]=="W":
        tmp += 1
        if tmp<ans:ans=tmp

    elif S[i-1]=="E" and S[i]=="W":
        pass

    elif S[i-1]=="E" and S[i]=="E":
        tmp -= 1
        if tmp<ans:ans=tmp



print(ans)
