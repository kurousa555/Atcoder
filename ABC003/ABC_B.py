from sys import stdin
S = list(input())
T = list(input())

for i in range(len(S)):
    if S[i]=="@" and  T[i] in ("a","t","c","o","d","e","r","@"):
        continue
    elif T[i]=="@" and  S[i] in ("a","t","c","o","d","e","r","@"):
        continue
    elif S[i]==T[i]:
        continue
    else:
        # print(S[i],T[i])
        print("You will lose")
        exit()
print("You can win")
        
