S = list(input())
set_S = set(S)

if len(set_S)==2:
    if S.count(list(set_S)[0])==2:
        if S.count(list(set_S)[1])==2:
            print("Yes")
            exit()
print("No")
