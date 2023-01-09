S =  list(input())
S.append(S[0])
del S[0]
print("".join(S))
