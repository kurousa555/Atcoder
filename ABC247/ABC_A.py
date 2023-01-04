S = list(input())
S.insert(0,"0")
del S[-1]
print("".join(S))
